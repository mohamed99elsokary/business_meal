from django.db.models import Q
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
        user = self.request.user
        if user.user_type == "client":
            return self.queryset.filter(user=user)
        elif user.user_type == "delivery":
            return self.queryset.filter(
                Q(Q(delivery_user=user) | Q(delivery_user__isnull=True)),
                user_address_isnull=False,
                is_check_out=True,
            )
        return self.queryset.filter(
            Q(Q(restaurant__admin=user) | Q(hotel__admin=user)),
            is_check_out=True,
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


class OrderItemViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.OrderItem.objects.all()
    serializer_class = serializers.AddOrderItemSerializer
