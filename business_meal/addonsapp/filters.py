from django_filters import rest_framework as filters

from . import models


class OptionsCategoryFilter(filters.FilterSet):
    hall = filters.CharFilter(method="pass_filter")
    meal = filters.CharFilter(method="pass_filter")
    package = filters.CharFilter(method="pass_filter")

    class Meta:
        model = models.OptionsCategory
        fields = ["restaurant", "hotel"]

    def pass_filter(self, queryset, name, value):
        return queryset
