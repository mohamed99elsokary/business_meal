from django.db.models import Q
from django_filters import rest_framework as filters

from . import models


class RestaurantFilter(filters.FilterSet):
    meal_category = filters.BaseInFilter(method="filter_by_meal_category")
    openbuffetpackage__category = filters.BaseInFilter(
        method="filter_by_openbuffetpackage__category"
    )

    class Meta:
        model = models.Restaurant
        fields = ["is_open_buffet"]

    def filter_by_meal_category(self, queryset, name, value):
        return queryset.filter(meal__category__in=value)

    def filter_by_openbuffetpackage__category(self, queryset, name, value):
        return queryset.filter(openbuffetpackage__category__in=value)


class MealFilter(filters.FilterSet):
    class Meta:
        model = models.Meal
        fields = ("restaurant",)


class MealOptionsFilter(filters.FilterSet):
    class Meta:
        model = models.MealOptions
        fields = ("meal", "is_additional")
