from django.db import models

from business_meal.addonsapp.models import Category, OptionsCategory
from business_meal.resturant_app.models import Restaurant

from .managers import OpenBuffetPackageQuerySet


class OpenBuffetPackage(models.Model):
    # relations
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True, default=None
    )

    # fields
    name = models.CharField(max_length=50, default=None, null=True, blank=True)
    description = models.TextField()
    clients_count = models.IntegerField()
    image = models.ImageField()
    price = models.IntegerField()
    objects: OpenBuffetPackageQuerySet = OpenBuffetPackageQuerySet.as_manager()

    def __str__(self):
        return f"{self.restaurant.name}"


class OpenBuffetPackageOptions(models.Model):
    # relations
    category = models.ForeignKey(
        OptionsCategory, on_delete=models.CASCADE, null=True, blank=True, default=None
    )
    package = models.ForeignKey(OpenBuffetPackage, on_delete=models.CASCADE)

    # fields
    option = models.CharField(max_length=50)
    is_additional = models.BooleanField(default=False)
    price = models.IntegerField(default=None, null=True, blank=True)
