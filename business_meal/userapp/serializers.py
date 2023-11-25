from bit68_notifications.models import ExpoDevice
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from business_meal.userapp.models import Address, User


class UserToken(serializers.Serializer):
    refersh_token = serializers.CharField(read_only=True)
    access_token = serializers.CharField(read_only=True)
    user_type = serializers.CharField(read_only=True)

    def create_user_token(self, user):
        refersh_token = RefreshToken.for_user(user)
        access_token = refersh_token.access_token
        return {
            "refersh_token": str(refersh_token),
            "access_token": str(access_token),
            "user_type": user.user_type,
        }


class ExpoDeviceSerializer(serializers.Serializer):
    registration_id = serializers.CharField(write_only=True)

    class Meta:
        model = ExpoDevice
        fields = ("registration_id",)

    def create(self, validated_data):
        user = self.context["request"].user

        if user.is_authenticated:
            user = user
        else:
            user = None

        device = ExpoDevice.objects.filter(
            registration_id=validated_data["registration_id"]
        ).first()
        if not device:
            device = ExpoDevice.objects.create(
                registration_id=validated_data["registration_id"]
            )
        device.user = user
        device.save()
        return device


class TinyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "phone"]


class UserSerializer(UserToken, serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
            "username",
            "password",
            "phone",
            "refersh_token",
            "access_token",
        ]
        extra_kwargs = {
            "email": {"write_only": True},
            "username": {"write_only": True},
            "password": {"write_only": True},
            "phone": {"write_only": True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return self.create_user_token(user)


class LoginSerializer(UserToken, serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        email = validated_data["email"]
        password = validated_data["password"]
        if user := authenticate(email=email, password=password):
            return self.create_user_token(user)
        raise serializers.ValidationError("email or password wrong")


class UpdatePhoneSerializer(UserToken, serializers.Serializer):
    phone = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user: User = self.context["request"].user
        user.new_phone = validated_data["phone"]
        user.send_otp(validated_data["phone"])
        user.save()


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "phone", "email", "is_new", "birth_date")


class GenerateUserSerializer(UserToken):
    def create(self, validated_data):
        last_user = User.objects.last()
        user = User.objects.create(is_active=True, email=f"{last_user.id}@guest.com")
        token = self.create_user_token(user)
        return {
            "access_token": token["access_token"],
            "refersh_token": token["refersh_token"],
        }


class AddressSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    location = serializers.ListField()

    class Meta:
        model = Address
        fields = "__all__"

    def create(self, validated_data):
        location = validated_data["location"]
        validated_data["location"] = f"SRID=4326;POINT ({location[0]} {location[1]})"
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if "location" in validated_data:
            location = validated_data["location"]
            validated_data[
                "location"
            ] = f"SRID=4326;POINT ({location[0]} {location[1]})"
        return super().update(instance, validated_data)


class VerifySerializer(UserToken, serializers.Serializer):
    phone = serializers.CharField(write_only=True, default="01111155856")
    otp = serializers.CharField(write_only=True, default=1234)

    def update_user(self, user):
        user.verification_code = None
        user.save()

    def create(self, validated_data):
        user = get_object_or_404(
            User,
            phone=validated_data["phone"],
            verification_code=validated_data["otp"],
        )
        self.update_user(user)
        return self.create_user_token(user)


class ValidateNewPhone(serializers.Serializer):
    otp = serializers.CharField(write_only=True, default=1234)

    def validate(self, attrs):
        user = self.context["request"].user
        if user.otp != attrs["otp"]:
            raise serializers.ValidationError({"detail": "wrong otp"})
        return super().validate(attrs)

    def create(self, validated_data):
        user: User = self.context["request"].user
        user.otp = None
        user.phone = user.new_phone
        user.new_phone = None
        user.save()


class RegisterLoginSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(write_only=True, default="01111155856")

    class Meta:
        model = User
        fields = ("phone", "is_new", "user_type")
        read_only_fields = ("is_new", "user_type")

    def create(self, validated_data):
        return User.create_user_or_login(validated_data)
