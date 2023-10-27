from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from bit68_notifications.models import ExpoDevice
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from business_meal.userapp import models
from business_meal.userapp.serializers import (
    AddressSerializer,
    ExpoDeviceSerializer,
    LoginSerializer,
    RegisterLoginSerializer,
    UserDataSerializer,
    UserSerializer,
    VerifySerializer,
)

from ..services.views import ModelViewSetClones


class UserViewSet(
    mixins.RetrieveModelMixin, ModelViewSetClones, viewsets.GenericViewSet
):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == "login":
            return LoginSerializer
        elif self.action in ["update_me", "get_me"]:
            return UserDataSerializer
        elif self.action == "register_login":
            return RegisterLoginSerializer
        elif self.action == "verify":
            return VerifySerializer
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
    def verify(self, request, *args, **kwargs):
        return super().create_clone(request, *args, **kwargs)


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
