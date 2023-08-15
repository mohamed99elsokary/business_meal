from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class OpenbuffetAppConfig(AppConfig):
    name = "business_meal.openbuffet_app"
    verbose_name = _("OpenbuffetApp")
