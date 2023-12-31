from django.contrib import admin
from solo.admin import SingletonModelAdmin
from unfold.admin import ModelAdmin, StackedInline

from business_meal.addonsapp.forms import SectionContentForm, SliderPictureForm
from business_meal.addonsapp.models import (
    ContactUs,
    PageSection,
    SectionContent,
    SiteConfiguration,
    SliderPicture,
)

from . import models

# SiteConfiguration


@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(ModelAdmin, SingletonModelAdmin):
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
class AdsAdmin(ModelAdmin):
    """Admin View for Ads"""


@admin.register(models.TermsAndConditions)
class TermsAndConditionsAdmin(ModelAdmin):
    """Admin View for TermsAndConditions"""


@admin.register(models.About)
class AboutAdmin(ModelAdmin):
    """Admin View for About"""
