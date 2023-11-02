from modeltranslation.translator import TranslationOptions, register

from .models import Meal, MealOptions, Restaurant


@register(Restaurant)
class RestaurantTranslationOptions(TranslationOptions):
    fields = ("description", "name")


@register(Meal)
class MealTranslationOptions(TranslationOptions):
    fields = ("description", "name")


@register(MealOptions)
class MealOptionsTranslationOptions(TranslationOptions):
    fields = ("option",)
