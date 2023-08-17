from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("open-buffet-package", views.OpenBuffetPackageViewSet)
router.register("open-buffet-package-options", views.OpenBuffetOptionsViewSet)
urlpatterns = [
    path("", include(router.urls)),
]
