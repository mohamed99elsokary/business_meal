from bit68_notifications.models import BulkNotification, ExpoDevice
from django.contrib import admin
from django.db.models import Q
from modeltranslation.admin import TranslationAdmin
from solo.admin import SingletonModelAdmin
from unfold.admin import ModelAdmin, StackedInline

from business_meal.addonsapp.forms import SectionContentForm, SliderPictureForm
from business_meal.addonsapp.models import (
    ContactUs,
    OptionsCategory,
    PageSection,
    PrivacyPolicy,
    SectionContent,
    SiteConfiguration,
    SliderPicture,
)

from . import models

# SiteConfiguration
admin.site.unregister(ExpoDevice)

admin.site.unregister(BulkNotification)


@admin.register(BulkNotification)
class BulkNotificationAdmin(ModelAdmin):
    """Admin View for BulkNotification"""


@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(ModelAdmin, TranslationAdmin):
    """Admin View for PrivacyPolicy"""


@admin.register(ExpoDevice)
class ExpoDeviceAdmin(ModelAdmin):
    """Admin View for ExpoDevice"""


@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(ModelAdmin):
    pass


# PageSection


class SectionContentInline(StackedInline):
    model = SectionContent
    form = SectionContentForm
    min_num = 0
    extra = 0
    classes = ["collapse"]


class SliderPictureInline(StackedInline):
    model = SliderPicture
    form = SliderPictureForm
    min_num = 0
    extra = 0
    classes = ["collapse"]


@admin.register(PageSection)
class PageSectionAdmin(ModelAdmin):
    list_display = ["id", "page_type", "section_number"]
    list_filter = ("page_type", "section_number")
    inlines = [SectionContentInline, SliderPictureInline]


# ContactUs


@admin.register(ContactUs)
class ContactUsAdmin(ModelAdmin):
    list_display = ("id", "name", "email", "phone_number", "subject", "message")
    search_fields = ("name", "email", "phone_number", "subject", "message")


@admin.register(models.Ads)
class AdsAdmin(ModelAdmin, TranslationAdmin):
    """Admin View for Ads"""


@admin.register(models.TermsAndConditions)
class TermsAndConditionsAdmin(ModelAdmin, TranslationAdmin):
    """Admin View for TermsAndConditions"""


@admin.register(models.About)
class AboutAdmin(ModelAdmin, TranslationAdmin):
    """Admin View for About"""


@admin.register(OptionsCategory)
class OptionsCategoryAdmin(ModelAdmin, TranslationAdmin):
    list_display = ("restaurant", "hotel", "name")

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(
            Q(Q(restaurant__admin=request.user) | Q(hotel__admin=request.user))
        )


class FilterForUserAdmin:
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs if request.user.is_superuser else qs.admin_filter(request.user)
