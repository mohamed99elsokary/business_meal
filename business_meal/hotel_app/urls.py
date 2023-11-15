from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("hotel", views.HotelViewSet)
router.register("hall", views.HotelHallViewSet)
router.register("hall-options", views.HallOptionsViewSet)
router.register("unavailable-hall-dates", views.UnavailableHallDatesViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
