from django_filters import rest_framework as filters

from . import models


class RestaurantFilter(filters.FilterSet):
    class Meta:
        model = models.Restaurant
        fields = ["is_open_buffet", "meal__category"]


class MealFilter(filters.FilterSet):
    class Meta:
        model = models.Meal
        fields = ("restaurant",)


class MealOptionsFilter(filters.FilterSet):
    class Meta:
        model = models.MealOptions
        fields = ("meal", "is_additional")
