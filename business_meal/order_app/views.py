from django.db.models import Q
from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..services.views import ModelViewSetClones
from . import models, serializers
from .conf import CANCELLED
from .filters import OrderFilter


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
    filterset_class = OrderFilter

    def get_queryset(self):
        user = self.request.user
        if user.user_type == "client":
            self.queryset = self.queryset.filter(user=user)
            if self.action == "list":
                self.queryset = self.queryset.filter(is_checkout=True)
            return self.queryset
        elif user.user_type == "delivery":
            return self.queryset.filter(
                Q(Q(delivery_user=user) | Q(delivery_user__isnull=True)),
                user_address__isnull=False,
                is_checkout=True,
            )
        return self.queryset.filter(
            Q(Q(restaurant__admin=user) | Q(hotel__admin=user)),
            is_checkout=True,
        )

    def get_serializer_class(self):
        if self.action in ["get_current_order", "retrieve", "list"]:
            return serializers.DetailedOrderSerializer
        elif self.action == "get_current_order":
            return serializers.CurrentOrderSerializer
        elif self.action in {"update", "partial_update"}:
            return serializers.UpdateOrderSerializer
        elif self.action == "checkout":
            return serializers.CheckoutSerializer
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

    @action(methods=["post"], detail=False)
    def checkout(self, request, *args, **kwargs):
        return self.create_clone(request, True, *args, **kwargs)

    @action(methods=["get"], detail=True)
    def accept_order(self, request, *args, **kwargs):
        order: models.Order = self.get_object()
        order.delivery_user = request.user
        order.save()
        return Response({"detail": "order accepted"})


class OrderItemViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.OrderItem.objects.all()
    serializer_class = serializers.AddOrderItemSerializer

    def get_serializer_class(self):
        if self.action in {"update", "partial_update"}:
            return serializers.UpdateOrderItemSerializer
        return super().get_serializer_class()


def payment(request, id):
    order = models.Order.objects.get(id=id)
    return render(request, "payment.html", {"total": (order.total) * 100})
