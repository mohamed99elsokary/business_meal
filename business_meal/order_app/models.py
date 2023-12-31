from django.db import models

from business_meal.resturant_app.models import Meal, MealOptions, PromoCode
from business_meal.userapp.models import Address, User

from ..hotel_app.models import Hotel
from ..resturant_app.models import Restaurant
from .conf import ORDER_CHOICES
from .model_mixins import OrderItemsMixin


class Order(models.Model):
    # relations
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="order_user")
    delivery_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="delivery_user",
        default=None,
        null=True,
        blank=True,
    )
    user_address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True,
    )
    promo = models.ForeignKey(
        PromoCode, on_delete=models.CASCADE, null=True, blank=True, default=None
    )
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, default=None, null=True, blank=True
    )
    hotel = models.ForeignKey(
        Hotel, on_delete=models.CASCADE, default=None, null=True, blank=True
    )
    # fields
    status = models.CharField(max_length=50, choices=ORDER_CHOICES)
    is_checkout = models.BooleanField()
    is_paid = models.BooleanField(default=False)
    payment_url = models.CharField(max_length=500, default=None, null=True, blank=True)
    note = models.TextField(default=None, null=True, blank=True)
    ordered_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    scheduled_time = models.DateTimeField(default=None, null=True, blank=True)
    estimated_time = models.DateTimeField(default=None, null=True, blank=True)
    delivered_time = models.DateTimeField(default=None, null=True, blank=True)


class OrderItem(OrderItemsMixin, models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="order_items"
    )
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    package = models.ForeignKey(
        "openbuffet_app.OpenBuffetPackage",
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True,
    )
    hall = models.ForeignKey(
        "hotel_app.Hall",
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True,
    )
    quantity = models.IntegerField()
    note = models.TextField(null=True, blank=True, default=None)


class OrderItemOption(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    meal_option = models.ForeignKey(
        MealOptions,
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True,
    )
    package_option = models.ForeignKey(
        "openbuffet_app.OpenBuffetPackageOptions",
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True,
    )
