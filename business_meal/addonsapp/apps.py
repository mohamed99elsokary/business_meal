from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AddonsappConfig(AppConfig):
    name = "business_meal.addonsapp"
    verbose_name = _("Addons App")
