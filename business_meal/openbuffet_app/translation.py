from modeltranslation.translator import TranslationOptions, register

from .models import OpenBuffetPackage, OpenBuffetPackageOptions


@register(OpenBuffetPackage)
class OpenBuffetPackageTranslationOptions(TranslationOptions):
    fields = ("description",)


@register(OpenBuffetPackageOptions)
class OpenBuffetPackageOptionsTranslationOptions(TranslationOptions):
    fields = ("option",)
