from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ResturantAppConfig(AppConfig):
    name = "business_meal.resturant_app"
    verbose_name = _("ResturantApp")
