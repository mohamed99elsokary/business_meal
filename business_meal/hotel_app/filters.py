from django_filters import rest_framework as filters

from . import models


class HotelFilter(filters.FilterSet):
    location = filters.CharFilter(method="annotate_distance")
    distance = filters.NumberFilter(method="filter_distance")

    class Meta:
        model = models.Hotel
        fields = ["rate"]

    def annotate_distance(self, queryset, name, value):
        return queryset.annotate_distance(value).order_by("distance")

    def filter_distance(self, queryset, name, value):
        return queryset.filter(distance__lte=value * 1000)
