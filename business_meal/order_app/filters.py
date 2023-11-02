from django_filters import rest_framework as filters

from . import models


class OrderFilter(filters.FilterSet):
    status = filters.BaseInFilter(method="filter_by_status")

    class Meta:
        model = models.Order
        fields = ["id"]

    def filter_by_status(self, queryset, name, value):
        return queryset.filter(status__in=value)
