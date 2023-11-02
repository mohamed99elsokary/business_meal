from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("order", views.OrderViewSet)
router.register("order-item", views.OrderItemViewSet)
urlpatterns = [
    path("", include(router.urls)),
    path("payment/<int:id>", views.payment),
]
