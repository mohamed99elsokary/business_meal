from django.db import models

from business_meal.resturant_app.models import Meal, MealOptions, PromoCode
from business_meal.userapp.models import Address, User


class Order(models.Model):
    # relations
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="order_user")
    delivery_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="delivery_user"
    )
    user_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    promo = models.ForeignKey(
        PromoCode, on_delete=models.CASCADE, null=True, blank=True, default=None
    )
    # fields
    type = models.CharField(max_length=50)
    status = models.CharField(
        max_length=50,
        choices=[
            ("preparing", "preparing"),
            ("delivering", "delivering"),
            ("delivered", "delivered"),
            ("canceled", "canceled"),
            ("is_paid", "is_paid"),
        ],
    )
    payment_type = models.CharField(max_length=50)
    is_checkout = models.BooleanField()
    is_paid = models.BooleanField(default=False)
    payment_url = models.CharField(max_length=50)
    note = models.CharField(max_length=50)
    ordered_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    scheduled_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    estimated_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    delivered_time = models.DateTimeField(auto_now=False, auto_now_add=False)


class OrderItem(models.Model):
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
    note = models.CharField(max_length=50)


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
