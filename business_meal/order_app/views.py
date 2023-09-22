from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from . import models, serializers


class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return serializers.DetailedOrderSerializer
        elif self.action == "get_current_order":
            return serializers.CurrentOrderSerializer
        return super().get_serializer_class()

    @action(methods=["get"], detail=False)
    def get_current_order(self, request, *args, **kwargs):
        order = models.Order.objects.get_or_create(user=request.user, is_checkout=False)
        serializer = self.get_serializer(order[0])
        return Response(serializer.data)
