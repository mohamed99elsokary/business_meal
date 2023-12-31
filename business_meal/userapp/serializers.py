from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from business_meal.userapp.models import Address, User


class UserToken(serializers.Serializer):
    refersh_token = serializers.CharField(read_only=True)
    access_token = serializers.CharField(read_only=True)

    def create_user_token(self, user):
        refersh_token = RefreshToken.for_user(user)
        access_token = refersh_token.access_token
        return {"refersh_token": str(refersh_token), "access_token": str(access_token)}


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


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "phone", "is_new")


class AddressSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Address
        fields = "__all__"


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


class RegisterLoginSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(write_only=True, default="01111155856")

    class Meta:
        model = User
        fields = ("phone", "is_new")
        read_only_fields = ("is_new",)

    def create(self, validated_data):
        return User.create_user_or_login(validated_data)
