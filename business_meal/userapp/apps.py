from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UserappConfig(AppConfig):
    name = "business_meal.userapp"
    verbose_name = _("User App")
