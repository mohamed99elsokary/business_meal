from decouple import config
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from ..addonsapp.serializers import PromoCodeSerializer
from ..hotel_app.serializers import HotelHallSerializer
from ..openbuffet_app.serializers import OpenBuffetPackageSerializer
from ..resturant_app.serializers import MealSerializer, TinyRestaurantSerializer
from ..userapp.serializers import TinyUserSerializer
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


class UpdateOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItem
        fields = "__all__"


class DetailedOrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, source="order_items")
    provider_name = serializers.SerializerMethodField()
    promo = PromoCodeSerializer()
    restaurant = TinyRestaurantSerializer()
    user = TinyUserSerializer()
    delivery_user = TinyUserSerializer()
    client_location = serializers.SerializerMethodField()
    restaurant_location = serializers.SerializerMethodField()

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

    def get_client_location(self, obj) -> list:
        return list(obj.user_address.location) if obj.user_address else None

    def get_restaurant_location(self, obj) -> list:
        if obj.user_address:
            from .model_mixins import get_branch_location

            branch = get_branch_location(obj) if obj.restaurant else None

            return list(branch.location) if branch else None


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = "__all__"


class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = ("user_address", "promo", "note", "scheduled_time", "status")

    def validate_hall_time(self, instance, validated_data):
        scheduled_time = validated_data["scheduled_time"]
        same_time_orders = (
            models.Order.objects.filter(
                scheduled_time__year=scheduled_time.year,
                scheduled_time__month=scheduled_time.month,
                scheduled_time__day=scheduled_time.day,
                hotel=instance.hotel,
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
        if instance.hotel and "scheduled_time" in validated_data:
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
        if validated_data["payment_type"] == "online_payment":
            base_url = config("BASE_URL", default=False, cast=str)
            order.payment_url = f"{base_url}en/api/payment/{order.id}/"
        order.save()
        return DetailedOrderSerializer(order).data
