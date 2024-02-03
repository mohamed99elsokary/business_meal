from decouple import config
from django.db.models import Q
from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..services.views import ModelViewSetClones
from . import models, serializers
from .conf import CANCELLED, CANCELLED_BY_USER
from .filters import OrderFilter
from .utils import confirm_payment


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

        elif self.action in {"update", "partial_update"}:
            return serializers.UpdateOrderSerializer
        elif self.action == "checkout":
            return serializers.CheckoutSerializer
        return super().get_serializer_class()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_checkout:
            if request.user == instance.user:
                instance.status = CANCELLED_BY_USER
            else:
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
        return self.create_clone(request, False, *args, **kwargs)

    @action(methods=["get"], detail=True)
    def accept_order(self, request, *args, **kwargs):
        order: models.Order = self.get_object()
        order.delivery_user = request.user
        # order.status = "delivering"
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
    base_url = config("BASE_URL", default=False, cast=str)
    PAYMENT_PUBLISH_KEY = config("PAYMENT_PUBLISH_KEY")

    return render(
        request,
        "payment.html",
        {
            "total": order.total * 100,
            "url": f"{base_url}en/api/gate-way-id/{id}",
            "api_key": PAYMENT_PUBLISH_KEY,
        },
    )


def update_order_gate_way_id(request, id):
    data = request.GET
    if confirm_payment(data["id"]):
        models.Order.objects.filter(id=id).update(
            is_paid=True, gate_way_id=data["id"], status="pending_confirmation"
        )
    else:
        models.Order.objects.filter(id=id).update(gate_way_id=data["id"])
    return Response({})
