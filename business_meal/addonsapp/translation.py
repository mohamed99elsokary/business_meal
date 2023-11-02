from modeltranslation.translator import TranslationOptions, register

from .models import About, Ads, Category, PrivacyPolicy, TermsAndConditions


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ("text",)


@register(Ads)
class AdsTranslationOptions(TranslationOptions):
    fields = ("name", "description")


@register(PrivacyPolicy)
class PrivacyPolicyTranslationOptions(TranslationOptions):
    fields = ("text",)


@register(TermsAndConditions)
class TermsAndConditionsTranslationOptions(TranslationOptions):
    fields = ("text",)
