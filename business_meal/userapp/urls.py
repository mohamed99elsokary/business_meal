from django.urls import include, path
from rest_framework import routers

from business_meal.userapp import views

router = routers.DefaultRouter()
router.register("users", views.UserViewSet, basename="users")
router.register("expo", views.ExpoDeviceViewSet, basename="expo")

router.register("address", views.AddressViewSet)
urlpatterns = [
    path("", include(router.urls)),
    path("users/facebook/", views.FacebookLogin.as_view(), name="fb_login"),
]
