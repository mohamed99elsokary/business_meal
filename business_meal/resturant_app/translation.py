from modeltranslation.translator import TranslationOptions, register

from .models import Meal, MealOptions, Restaurant


@register(Restaurant)
class RestaurantTranslationOptions(TranslationOptions):
    fields = ("description",)


@register(Meal)
class MealTranslationOptions(TranslationOptions):
    fields = ("description",)


@register(MealOptions)
class MealOptionsTranslationOptions(TranslationOptions):
    fields = ("option",)
