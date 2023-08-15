from django.urls import include, path
from rest_framework import routers

from business_meal.userapp.views import (UserViewSet,FacebookLogin)

router = routers.DefaultRouter()
router.register("users", UserViewSet, basename="users")

router.register('address',views.AdressViewSet)
urlpatterns = [
    path("", include(router.urls)),
    path("users/facebook/", FacebookLogin.as_view(), name="fb_login"),
]
