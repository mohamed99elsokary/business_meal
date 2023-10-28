from django.shortcuts import get_object_or_404
from rest_framework import serializers

from ..addonsapp.serializers import PromoCodeSerializer
from ..hotel_app.serializers import HotelHallSerializer
from ..openbuffet_app.serializers import OpenBuffetPackageSerializer
from ..resturant_app.serializers import MealSerializer
from . import models


class CurrentOrder:
    requires_context = True

    def __call__(self, serializer_field):
        user = serializer_field.context["request"].user
        order = models.Order.objects.get_or_create(user=user, is_checkout=False)
        return order[0]

    def __repr__(self):
        return f"{self.__class__.__name__}()"


class OrderItemOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItemOption
        exclude = ("order_item",)


class OrderItemSerializer(serializers.ModelSerializer):
    options = OrderItemOptionsSerializer(many=True, source="orderitemoption_set")
    meal = MealSerializer()
    hall = HotelHallSerializer()
    package = OpenBuffetPackageSerializer()

    class Meta:
        model = models.OrderItem
        fields = "__all__"


class AddOrderItemSerializer(serializers.ModelSerializer):
    order = serializers.HiddenField(default=CurrentOrder())
    options = OrderItemOptionsSerializer(many=True, write_only=True, required=False)

    class Meta:
        model = models.OrderItem
        fields = "__all__"

    def validate(self, attrs):
        order = attrs.get("order")
        meal = attrs.get("meal")
        package = attrs.get("package")
        hall = attrs.get("hall")
        if not meal and not package and not hall:
            raise serializers.ValidationError(
                {"detail": "you have to select meal, package or hall."}
            )
        if order.hotel or order.restaurant:
            if meal and order.restaurant != meal.restaurant:
                raise serializers.ValidationError(
                    {
                        "detail": "you can't order from two different restaurants in the same order"
                    }
                )
            elif package and order.restaurant != package.restaurant:
                raise serializers.ValidationError(
                    {
                        "detail": "you can't order from two different restaurants in the same order"
                    }
                )
            elif hall and order.hotel != hall.hotel:
                raise serializers.ValidationError(
                    {
                        "detail": "you can't order from two different hotels in the same order"
                    }
                )
        return super().validate(attrs)

    def create(self, validated_data):
        if validated_data.get("options"):
            options_data = validated_data.pop("options", [])
        order_item = super().create(validated_data)
        if validated_data.get("options"):
            models.OrderItemOption.objects.bulk_create(
                [
                    models.OrderItemOption(order_item=order_item, **option_data)
                    for option_data in options_data
                ]
            )

        return order_item


class DetailedOrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, source="order_items")
    provider_name = serializers.SerializerMethodField()
    promo = PromoCodeSerializer()

    class Meta:
        model = models.Order
        fields = "__all__"

    def get_provider_name(self, obj) -> str:
        if obj.restaurant:
            return obj.restaurant.name
        elif obj.hotel:
            return obj.hotel.name
        else:
            return ""


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = "__all__"


class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = (
            "user_address",
            "promo",
            "note",
            "scheduled_time",
        )

    def validate_hall_time(self, instance, validated_data):
        if "scheduled_time" in validated_data:
            scheduled_time = validated_data["scheduled_time"]
        elif instance.scheduled_time:
            scheduled_time = instance.scheduled_time
        same_time_orders = (
            models.Order.objects.filter(
                scheduled_time=scheduled_time, hotel=instance.hotel
            )
            .exclude(id=instance.id)
            .values_list("id", flat=True)
        )
        if same_time_orders.count() > 0:
            same_time_halls = models.OrderItem.objects.filter(
                order__in=same_time_orders, hall=instance.hall
            )
            if same_time_halls.count() > 0:
                raise serializers.ValidationError(
                    {"detail": "sorry this time is reserved already"}
                )

    def update(self, instance, validated_data):
        if instance.hotel:
            self.validate_hall_time(instance, validated_data)
        return super().update(instance, validated_data)


class CheckoutSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = models.Order
        fields = ("id", "payment_type")

    def create(self, validated_data):
        user = self.context["request"].user
        order = get_object_or_404(models.Order, id=validated_data["id"], user=user)
        order.payment_type = validated_data["payment_type"]
        order.save()
        return order
