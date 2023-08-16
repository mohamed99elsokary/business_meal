from rest_framework import viewsets

from . import filters, models, serializers


class RestaurantViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Restaurant.objects.all()
    serializer_class = serializers.RestaurantSerializer
    ordering = ("rate",)
    search_fields = ["name"]
    filterset_class = filters.RestaurantFilter
