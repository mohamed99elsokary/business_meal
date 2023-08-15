from typing import Any

from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from business_meal.userapp.models import Address, User


class UserSerializer(serializers.ModelSerializer):
    refersh_token = serializers.CharField(read_only=True)
    access_token = serializers.CharField(read_only=True)

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
        user.is_active = True
        user.save()
        refersh_token = RefreshToken.for_user(user)
        access_token = refersh_token.access_token
        return {"refersh_token": refersh_token, "access_token": access_token}


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    access_token = serializers.CharField(read_only=True)
    refersh_token = serializers.CharField(read_only=True)

    def create(self, validated_data: Any) -> Any:
        email = validated_data["email"]
        password = validated_data["password"]
        user = authenticate(email=email, password=password)
        if user:
            refersh_token = RefreshToken.for_user(user)
            access_token = refersh_token.access_token
            return {
                "refersh_token": refersh_token,
                "access_token": access_token,
            }
        raise serializers.ValidationError("email or password wrong")


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "phone")


class AddressSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Address
        fields = "__all__"
