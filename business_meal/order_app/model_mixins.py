from django.contrib.gis.db.models.functions import Distance
from django.utils import timezone
from django_lifecycle import (
    AFTER_CREATE,
    AFTER_SAVE,
    BEFORE_CREATE,
    BEFORE_UPDATE,
    LifecycleModelMixin,
    hook,
)

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
    def recalculate_order_price(self):
        price = 0
        if self.meal:
            price = self.meal.price
        elif self.package:
            price = self.package.price
        elif self.hall:
            price = self.hall.price
        self.order.total += price * self.quantity
        self.order.save()


class OrderItemOptionMixin(LifecycleModelMixin):
    @hook(AFTER_CREATE)
    def recalculate_order_price(self):
        order = self.order_item.order
        price = 0
        if self.meal_option:
            price = self.meal_option.price
        elif self.package_option:
            price = self.package_option.price
        order.total += price * self.quantity
        order.save()


def get_branch_location(order):
    from ..resturant_app.models import Branch

    user_location = order.user_address.location
    return (
        Branch.objects.filter(restaurant=order.restaurant)
        .annotate(distance=Distance("location", user_location))
        .order_by("distance")
    ).first()


class OrderMixin(LifecycleModelMixin):
    @hook(AFTER_CREATE, when="promo", has_changed=True)
    def recalculate_order_price(self):
        if self.promo.discount_type == "amount":
            self.total -= self.promo.discount
        else:
            discount_amount = self.total * (self.promo.discount / 100)
            self.total -= discount_amount
        self.save()

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

    @hook(BEFORE_UPDATE, when="payment_type", has_changed=True)
    def update_is_checkout(self):
        self.is_checkout = True
        self.ordered_time = timezone.now()
        if self.payment_type == "online_payment":
            self.status = "pending_payment"
        else:
            self.status = "pending_confirmation"

        self.save(skip_hooks=True)

    @hook(BEFORE_UPDATE, when="status", has_changed=True)
    def send_notification(self):
        from ..addonsapp.utils import NotificationHandler

        NotificationHandler(
            users=[self.user],
            title="your order status has been updated",
            body="Your order status has been updated",
            is_in_app=True,
            is_push_notification=True,
        )

    def get_provider_admin_id(self):
        if self.restaurant:
            return self.restaurant.admin.id
        elif self.hotel:
            return self.hotel.admin.id
        else:
            return None

    @hook(AFTER_SAVE, when="status", is_now="pending_confirmation")
    def send_notification(self):
        from django.db.models import Q

        from ..addonsapp.utils import NotificationHandler
        from ..userapp.models import User

        users = User.objects.filter(
            Q(user_type="delivery") | Q(id=self.get_provider_admin_id())
        )
        NotificationHandler(
            users=users,
            title="your order status has been updated",
            body="Your order status has been updated",
            is_in_app=True,
            is_push_notification=True,
        )

    @hook(AFTER_SAVE, when="status", was_not="cancelled", is_now="cancelled")
    def send_notification(self):
        payment_refund(id=self.gate_way_id, amount=self.total)
