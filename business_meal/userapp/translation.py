from modeltranslation.translator import TranslationOptions, register

from .models import DeliveryCar


@register(DeliveryCar)
class DeliveryCarTranslationOptions(TranslationOptions):
    fields = ("model",)
