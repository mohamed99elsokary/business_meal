from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
# router.register("path", views.)
router.register("restaurant", views.RestaurantViewSet)
router.register("meal", views.MealViewSet)
router.register("meal-options", views.MealOptionsViewSet)
router.register("branch", views.BranchViewSet)
urlpatterns = [
    path("", include(router.urls)),
]
