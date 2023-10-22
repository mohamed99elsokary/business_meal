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


class OrderItemOptionMixin(LifecycleModelMixin):
    @hook(AFTER_CREATE)
    def recalculate_order_price(self):
        order = self.order_item.order
        price = 0
        if self.meal_option:
            price = self.meal_option.price
        elif self.package_option:
            price = self.package_option.price
        order.total += price
        order.save()


class OrderMixin(LifecycleModelMixin):
    @hook(AFTER_CREATE, when="promo", has_changed=True)
    def recalculate_order_price(self):
        if self.promo.discount_type == "amount":
            self.total -= self.promo.discount
        else:
            discount_amount = self.total * (self.promo.discount / 100)
            self.total -= discount_amount
        self.save()
