from modeltranslation.translator import TranslationOptions, register

from .models import Hall, HallOptions, Hotel


@register(Hotel)
class HotelTranslationOptions(TranslationOptions):
    fields = ("description", "name", "address")


@register(Hall)
class HallTranslationOptions(TranslationOptions):
    fields = ("description", "name")


@register(HallOptions)
class HallOptionsTranslationOptions(TranslationOptions):
    fields = ("option",)
