from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("hotel", views.HotelViewSet)
router.register("hall", views.HotelHallViewSet)
urlpatterns = [
    path("", include(router.urls)),
]
