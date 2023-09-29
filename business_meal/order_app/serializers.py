from rest_framework import serializers

from . import models


class CurrentOrder:
    requires_context = True

    def __call__(self, serializer_field):
        user = serializer_field.context["request"].user
        order = models.Order.objects.get_or_create(user=user, is_checkout=False)
        return order[0]

    def __repr__(self):
        return "%s()" % self.__class__.__name__


class OrderItemOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItemOption
        exclude = ("order_item",)


class OrderItemSerializer(serializers.ModelSerializer):
    options = OrderItemOptionsSerializer(many=True, source="orderitemoption_set")

    class Meta:
        model = models.OrderItem
        fields = "__all__"


class AddOrderItemSerializer(serializers.ModelSerializer):
    order = serializers.HiddenField(default=CurrentOrder())
    options = OrderItemOptionsSerializer(many=True, write_only=True)

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
        options_data = validated_data.pop("options", [])
        order_item = super().create(validated_data)
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

    class Meta:
        model = models.Order
        fields = "__all__"

    def get_provider_name(self, obj) -> str:
        return obj.restaurant.name if obj.restaurant else obj.hotel.name


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
