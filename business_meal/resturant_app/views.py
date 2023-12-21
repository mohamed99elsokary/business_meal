from django.db.models import Q
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from . import filters, models, serializers


class RestaurantViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Restaurant.objects.all()
    serializer_class = serializers.RestaurantSerializer
    ordering = ("rate",)
    search_fields = ["name"]
    filterset_class = filters.RestaurantFilter


class MealViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Meal.objects.all().select_related("category")
    serializer_class = serializers.MealSerializer
    filterset_class = filters.MealFilter
    pagination_class = None


class MealOptionsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.MealOptions.objects.all()
    serializer_class = serializers.MealOptionsSerializer
    filterset_class = filters.MealOptionsFilter
    pagination_class = None


class BranchViewSet(viewsets.ModelViewSet):
    queryset = models.Branch.objects.all()
    serializer_class = serializers.BranchSerializer
    filterset_class = filters.BranchFilter

    def get_queryset(self):
        if self.action == "my_branches":
            return self.queryset.filter(
                Q(restaurant__admin=self.user) | Q(admin=self.user)
            )
        return super().get_queryset()

    @action(methods=["get"], detail=False)
    def my_branches(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        return Response(serializer.data)
