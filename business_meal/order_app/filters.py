from django_filters import rest_framework as filters

from . import models


class OrderFilter(filters.FilterSet):
    status = filters.BaseInFilter(method="filter_by_status")
    location = filters.CharFilter(method="annotate_distance")
    distance = filters.NumberFilter(method="filter_distance")

    class Meta:
        model = models.Order
        fields = ["id", "delivery_user"]

    def filter_by_status(self, queryset, name, value):
        return queryset.filter(status__in=value)

    def filter_distance(self, queryset, name, value):
        return queryset.filter(distance__lte=value * 1000)

    def annotate_distance(self, queryset, name, value):
        return queryset.annotate_distance(value).order_by("distance")
