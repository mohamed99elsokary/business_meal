from django.contrib.gis.db.models.functions import Distance
from django_lifecycle import (
    AFTER_CREATE,
    AFTER_SAVE,
    BEFORE_CREATE,
    BEFORE_UPDATE,
    LifecycleModelMixin,
    hook,
)


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
                branch = get_branch_location(self)
                self.delivery_fee = branch.distance.km * 10
                self.total += self.delivery_fee
                self.save(skip_hooks=True)

    @hook(BEFORE_UPDATE, when="payment_type", has_changed=True)
    def update_is_checkout(self):
        self.is_checkout = True
        self.save(skip_hooks=True)
