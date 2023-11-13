from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("page-sections", views.PageSectionViewSet)
router.register("contact-us", views.ContactUsViewset)
router.register("adds", views.AdsViewSet)
router.register("category", views.CategoryViewSet)
router.register("promocode", views.PromoCodeViewSet)
router.register("privacy-policy", views.PrivacyPolicyViewSet)
router.register("about", views.AboutViewSet)
router.register("terms-and-conditions", views.TermsAndConditionsViewSet)
router.register('options-categories',views.OptionsCategoryViewSet)
urlpatterns = [
    path("", include(router.urls)),
]
