from django.contrib.gis.db import models as gis_model
from django.db import models

from ..addonsapp.models import Category, OptionsCategory, PromoCode
from ..userapp.models import User
from .managers import BranchQuerySet


class Restaurant(models.Model):
    # relations
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    # fields
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="media/")
    cover_photo = models.ImageField(
        upload_to="media/", null=True, blank=True, default=None
    )
    description = models.CharField(max_length=50)
    is_open_buffet = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    rate = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Branch(models.Model):
    # relations
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    # fields
    phone = models.CharField(max_length=50)
    location = gis_model.PointField(srid=4326, blank=True, null=True)
    street = models.CharField(max_length=50)
    building = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)
    max_orders = models.IntegerField()
    delivery_fees = models.FloatField(default=0)
    estimated_mins = models.FloatField(default=0)
    objects: BranchQuerySet = BranchQuerySet.as_manager()

    def __str__(self):
        return f"{self.restaurant} {self.street}"


class Meal(models.Model):
    # relations
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True, default=None
    )
    # fields
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media/")
    description = models.CharField(max_length=50)
    price = models.IntegerField()
    is_available = models.BooleanField(default=True)
    is_top_dish = models.BooleanField(default=False)
    is_share_box = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class MealOptions(models.Model):
    # relations
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    category = models.ForeignKey(
        OptionsCategory, on_delete=models.CASCADE, null=True, blank=True, default=None
    )
    # fields
    option = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    is_additional = models.BooleanField(default=False)

    def __str__(self):
        return self.option
