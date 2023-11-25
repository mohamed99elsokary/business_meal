from decouple import config
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from ..addonsapp.serializers import PromoCodeSerializer
from ..hotel_app.models import HallBusyDate
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
        else:
            options_data = None
        order_item = super().create(validated_data)
        if options_data:
            models.OrderItemOption.objects.bulk_create(
                [
                    models.OrderItemOption(order_item=order_item, **option_data)
                    for option_data in options_data
                ]
            )
            validated_data["order"].recalculate_price()

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
    estimated_mins = serializers.SerializerMethodField()
    distance = serializers.SerializerMethodField()

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
        return list(obj.branch.location) if obj.branch else None

    def get_estimated_mins(self, obj) -> int:
        return obj.branch.estimated_mins if obj.branch else None

    def get_distance(self, obj) -> float:
        return obj.distance.km if "distance" in dir(obj) and obj.distance else None


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
            "status",
            "scheduled_time",
            "estimated_time",
            "delivered_time",
            "preparing_time",
            "ready_to_delivery_time",
            "picked_time",
            "arrived_to_restaurant_time",
            "begin_trip_time",
        )

    def validate_hall_time(self, instance, validated_data):
        scheduled_time = validated_data["scheduled_time"]
        hall = models.OrderItem.objects.filter(order=instance).values("hall")
        if hall:
            hall = hall.first()["hall"]
        same_time_halls = models.OrderItem.objects.filter(
            hall=hall,
            order__scheduled_time__year=scheduled_time.year,
            order__scheduled_time__month=scheduled_time.month,
            order__scheduled_time__day=scheduled_time.day,
        )

        if same_time_halls.count() > 0:
            raise serializers.ValidationError(
                {"detail": "sorry this time is reserved already"}
            )

        busy_hall_times = HallBusyDate.objects.filter(
            Hall=hall,
            date__year=scheduled_time.year,
            date__month=scheduled_time.month,
            date__day=scheduled_time.day,
        )
        if busy_hall_times.count() > 0:
            raise serializers.ValidationError(
                {"detail": "sorry hall is busy at this time"}
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

    def validate_branch_is_busy(self, order):
        if order.branch and not order.branch.is_available:
            raise serializers.ValidationError(
                {"detail": "sorry the restaurant is busy at this time"}
            )

    def create(self, validated_data):
        user = self.context["request"].user
        order = get_object_or_404(models.Order, id=validated_data["id"], user=user)
        self.validate_branch_is_busy(order)
        order.payment_type = validated_data["payment_type"]
        if validated_data["payment_type"] == "online_payment":
            base_url = config("BASE_URL", default=False, cast=str)
            order.payment_url = f"{base_url}en/api/payment/{order.id}"
        order.save()
        return DetailedOrderSerializer(order).data
