from rest_framework import serializers

from . import models


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItem
        fields = "__all__"


class DetailedOrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, source="order_items")

    class Meta:
        model = models.Order
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = "__all__"


class CurrentOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField()
