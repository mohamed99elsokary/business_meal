from django_lifecycle import AFTER_CREATE, BEFORE_CREATE, LifecycleModelMixin, hook


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
        self.order.total += price
        self.order.save()
