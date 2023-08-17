from rest_framework import viewsets

from . import filters, models, serializers


class RestaurantViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Restaurant.objects.all()
    serializer_class = serializers.RestaurantSerializer
    ordering = ("rate",)
    search_fields = ["name"]
    filterset_class = filters.RestaurantFilter


class MealViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = query = models.Meal.objects.all().select_related("category")
    serializer_class = serializers.MealSerializer
    filterset_class = filters.MealFilter
    pagination_class = None
