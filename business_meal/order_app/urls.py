from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("order", views.OrderViewSet)
router.register("order-item", views.OrderItemViewSet)
router.register("rates", views.RatesViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("payment/<int:id>", views.payment),
    path("gate-way-id/<int:id>", views.update_order_gate_way_id),
]
