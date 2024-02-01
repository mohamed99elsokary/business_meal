from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from bit68_notifications.models import ExpoDevice
from dj_rest_auth.registration.views import SocialLoginView
from django.db.models import Sum
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..order_app.models import Order
from ..services.views import ModelViewSetClones
from . import models
from .serializers import (
    AddressSerializer,
    ExpoDeviceSerializer,
    GenerateUserSerializer,
    LoginSerializer,
    RegisterLoginSerializer,
    UpdatePhoneSerializer,
    UpdateUserDataSerializer,
    UserDataSerializer,
    UserSerializer,
    ValidateNewPhone,
    VerifySerializer,
)


class UserViewSet(
    mixins.RetrieveModelMixin, ModelViewSetClones, viewsets.GenericViewSet
):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == "login":
            return LoginSerializer
        elif self.action == "get_me":
            return UserDataSerializer
        elif self.action == "update_me":
            return UpdateUserDataSerializer
        elif self.action == "register_login":
            return RegisterLoginSerializer
        elif self.action == "verify":
            return VerifySerializer
        elif self.action == "generate_user":
            return GenerateUserSerializer
        elif self.action == "update_phone":
            return UpdatePhoneSerializer
        elif self.action == "validate_new_phone":
            return ValidateNewPhone
        return super().get_serializer_class()

    @action(methods=["post"], detail=False)
    def register(self, request, *args, **kwargs):
        return super().create_clone(request, *args, **kwargs)

    @action(methods=["post"], detail=False)
    def login(self, request, *args, **kwargs):
        return super().create_clone(request, data=False, *args, **kwargs)

    @action(methods=["get"], detail=False)
    def get_me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    @action(methods=["post"], detail=False)
    def generate_user(self, request, *args, **kwargs):
        return super().create_clone(request, *args, **kwargs)

    @action(methods=["put"], detail=False)
    def update_me(self, request):
        instance = request.user
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(methods=["delete"], detail=False)
    def delete_me(self, request):
        request.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=["post"], detail=False)
    def register_login(self, request, *args, **kwargs):
        return super().create_clone(request, *args, **kwargs)

    @action(methods=["post"], detail=False)
    def update_phone(self, request, *args, **kwargs):
        return super().create_clone(request, data=False, *args, **kwargs)

    @action(methods=["post"], detail=False)
    def validate_new_phone(self, request, *args, **kwargs):
        return super().create_clone(request, data=False, *args, **kwargs)

    @action(methods=["post"], detail=False)
    def verify(self, request, *args, **kwargs):
        return super().create_clone(request, *args, **kwargs)

    @action(methods=["get"], detail=False)
    def total_delivery(self, request, *args, **kwargs):
        user_orders = Order.objects.filter(
            delivery_user=request.user, status="delivered"
        )
        total_delivery_fees = user_orders.aggregate(fee=Sum("delivery_fee"))["fee"]
        return Response({"total_delivery": total_delivery_fees})


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class AddressViewSet(viewsets.ModelViewSet):
    queryset = models.Address.objects.all()
    serializer_class = AddressSerializer

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class ExpoDeviceViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = ExpoDevice.objects.all()
    serializer_class = ExpoDeviceSerializer
