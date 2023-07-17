from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ServicesappConfig(AppConfig):
    name = "business_meal.services"
    verbose_name = _("Services App")
