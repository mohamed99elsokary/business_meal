from django.contrib.gis.db.models.functions import Distance
from django.db.models import F, Q, Sum, Value
from django.db.models.functions import Coalesce
from django.utils import timezone
from django_lifecycle import (
    AFTER_CREATE,
    AFTER_SAVE,
    BEFORE_CREATE,
    BEFORE_SAVE,
    BEFORE_UPDATE,
    LifecycleModelMixin,
    hook,
)

from ..addonsapp.utils import NotificationHandler
from .utils import payment_refund


class OrderItemsMixin(LifecycleModelMixin):
    @hook(BEFORE_CREATE)
    def add_provider_to_order(self):
        order = self.order
        if not order.hotel and not order.restaurant:
            if self.meal:
                order.restaurant = self.meal.restaurant
            elif self.package:
                order.restaurant = self.package.restaurant
            elif self.hall:
                order.hotel = self.hall.hotel
        order.save()

    @hook(AFTER_CREATE)
    def order_price(self):
        self.order.recalculate_order_price()


class OrderItemOptionMixin(LifecycleModelMixin):
    @hook(AFTER_CREATE)
    def order_price(self):
        order = self.order_item.order
        order.recalculate_order_price()


def get_branch_location(order):
    from ..resturant_app.models import Branch

    user_location = order.user_address.location
    return (
        Branch.objects.filter(restaurant=order.restaurant)
        .annotate(distance=Distance("location", user_location))
        .order_by("distance")
    ).first()


class OrderMixin(LifecycleModelMixin):
    @hook(AFTER_SAVE, when="promo", has_changed=True)
    def order_price(self):
        self.recalculate_order_price()

    @hook(AFTER_SAVE, when="user_address", has_changed=True)
    def calculate_delivery_fees(self):
        if self.restaurant:
            if not self.user_address:
                self.total -= self.delivery_fee
                self.delivery_fee = 0
                return self.save(skip_hooks=True)
            else:
                self.branch = get_branch_location(self)
                self.delivery_fee = self.branch.distance.km * self.branch.delivery_fees
                self.total += self.delivery_fee
                self.save(skip_hooks=True)

    def calculate_loyalty_points(self):
        self.user.loyalty_points += int(self.total / 8)
        self.user.save()

    @hook(BEFORE_UPDATE, when="payment_type", has_changed=True)
    def update_is_checkout(self):
        self.is_checkout = True
        self.ordered_time = timezone.now()
        self.calculate_loyalty_points()
        if self.payment_type == "online_payment":
            self.status = "pending_payment"
        else:
            self.status = "pending_confirmation"

        self.save()

    def get_provider_admin_id(self):
        if self.restaurant:
            return self.restaurant.admin.id
        elif self.hotel:
            return self.hotel.admin.id
        else:
            return None

    @hook(BEFORE_UPDATE, when="status", has_changed=True, is_now="ready_for_pickup")
    def send_ready_for_pickup_notification(self):
        from ..userapp.models import User

        users = User.objects.filter(user_type="delivery")
        NotificationHandler(
            users=users,
            title="there are orders waiting for your service",
            body="there are orders waiting for your service",
            is_in_app=True,
            is_push_notification=True,
        )

    @hook(BEFORE_SAVE, when="status",has_changed=True, is_now="pending_confirmation")
    def send_pending_confirmation_notification(self):
        from ..userapp.models import User

        users = User.objects.filter(
             id=self.get_provider_admin_id()
        )
        NotificationHandler(
            users=users,
            title="there is an order that waiting your confirmation",
            body="there is an order that waiting your confirmation",
            is_in_app=True,
            is_push_notification=True,
        )

    @hook(
        AFTER_SAVE,
        when="status",
        has_changed=True,
        was_not="cancelled",
        is_now="cancelled",
    )
    def send_notification(self):
        payment_refund(id=self.gate_way_id, amount=self.total)
        NotificationHandler(
            users=[self.user],
            title="your order status has been cancelled",
            body="Your order status has been cancelled",
            is_in_app=True,
            is_push_notification=True,
        )

    @hook(BEFORE_UPDATE, when="status", has_changed=True, is_not="cancelled")
    def send_notification_to_order_user(self):
        notification_data = f"your order status has been updated to {self.status}"
        NotificationHandler(
            users=[self.user],
            title=notification_data,
            body=notification_data,
            is_in_app=True,
            is_push_notification=True,
        )

    def recalculate_order_price(self):
        from .models import OrderItem, OrderItemOption

        order_items_price = (
            (
                OrderItem.objects.filter(order=self).annotate(
                    price=(
                        Coalesce(F("meal__price"), Value(0))
                        + Coalesce(F("package__price"), Value(0))
                        + Coalesce(F("hall__price"), Value(0))
                    )
                    * F("quantity")
                )
            ).aggregate(total_price=Sum("price"))
        )["total_price"] or 0
        items_options_price = (
            (
                OrderItemOption.objects.filter(order_item__order=self).annotate(
                    price=(
                        Coalesce(F("meal_option__price"), Value(0))
                        + Coalesce(F("package_option__price"), Value(0))
                        + Coalesce(F("hall_option__price"), Value(0))
                    )
                    * F("quantity")
                )
            ).aggregate(total_price=Sum("price"))
        )["total_price"] or 0

        print("___________________________________")
        total_before_promo = order_items_price + items_options_price + self.delivery_fee
        if promo := self.promo:
            if promo.discount_type == "amount":
                total_after_promo = total_before_promo - promo.discount
            else:
                total_after_promo = (
                    total_before_promo - promo.discount * total_before_promo
                )
            self.total = total_after_promo
            return self.save()
        self.total = total_before_promo
        return self.save()
