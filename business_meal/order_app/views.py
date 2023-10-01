from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..services.views import ModelViewSetClones
from . import models, serializers
from .conf import CANCELLED


class OrderViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
    ModelViewSetClones,
):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ["get_current_order", "retrieve"]:
            return serializers.DetailedOrderSerializer
        elif self.action == "get_current_order":
            return serializers.CurrentOrderSerializer
        elif self.action in {"update", "partial_update"}:
            return serializers.UpdateOrderSerializer
        return super().get_serializer_class()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_checkout:
            instance.status = CANCELLED
            instance.save()
        else:
            instance.delete()
        return Response(status=200)

    @action(methods=["get"], detail=False)
    def get_current_order(self, request, *args, **kwargs):
        order = models.Order.objects.get_or_create(user=request.user, is_checkout=False)
        serializer = self.get_serializer(order[0])
        return Response(serializer.data)


class OrderItemViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.OrderItem.objects.all()
    serializer_class = serializers.AddOrderItemSerializer
