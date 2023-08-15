from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
# router.register("path", views.)
router.register("order", views.OrderViewSet)
urlpatterns = [
    path("", include(router.urls)),
]
