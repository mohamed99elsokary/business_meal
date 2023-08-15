from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("page-sections", views.PageSectionViewSet)
router.register("contact-us", views.ContactUsViewset)


router.register("adds", views.AdsViewSet)
router.register('category',views.CategoryViewSet)
urlpatterns = [
    path("", include(router.urls)),
]
