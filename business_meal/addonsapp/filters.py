from django_filters import rest_framework as filters

from . import models


class OptionsCategoryFilter(filters.FilterSet):
    class Meta:
        model = models.OptionsCategory
        fields = ["restaurant", "hotel"]
