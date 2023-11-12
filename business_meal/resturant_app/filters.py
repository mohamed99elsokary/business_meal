from django_filters import rest_framework as filters

from . import models


class RestaurantFilter(filters.FilterSet):
    meal_category = filters.BaseInFilter(method="filter_by_meal_category")
    openbuffetpackage__category = filters.BaseInFilter(
        method="filter_by_openbuffetpackage__category"
    )

    class Meta:
        model = models.Restaurant
        fields = ["is_open_buffet", "meal__is_share_box"]

    def filter_by_meal_category(self, queryset, name, value):
        return queryset.filter(meal__category__in=value)

    def filter_by_openbuffetpackage__category(self, queryset, name, value):
        return queryset.filter(openbuffetpackage__category__in=value)


class MealFilter(filters.FilterSet):
    class Meta:
        model = models.Meal
        fields = ("restaurant", "category", "is_share_box")


class MealOptionsFilter(filters.FilterSet):
    class Meta:
        model = models.MealOptions
        fields = ("meal", "is_additional")


class BranchFilter(filters.FilterSet):
    meal_category = filters.BaseInFilter(method="filter_by_meal_category")
    openbuffetpackage__category = filters.BaseInFilter(
        method="filter_by_openbuffetpackage__category"
    )
    location = filters.CharFilter(method="annotate_distance")
    distance = filters.NumberFilter(method="filter_distance")

    class Meta:
        model = models.Branch
        fields = (
            "restaurant",
            "restaurant__is_open_buffet",
            "restaurant__meal__is_share_box",
        )

    def filter_distance(self, queryset, name, value):
        return queryset.filter(distance__lte=value * 1000)

    def annotate_distance(self, queryset, name, value):
        return queryset.annotate_distance(value).order_by("distance")

    def filter_by_meal_category(self, queryset, name, value):
        return queryset.filter(restaurant__meal__category__in=value)

    def filter_by_openbuffetpackage__category(self, queryset, name, value):
        return queryset.filter(restaurant__openbuffetpackage__category__in=value)
