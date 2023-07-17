from functools import partial

from django.db import models
from django.utils.translation import gettext_lazy as _
from solo.models import SingletonModel

from business_meal.addonsapp.conf import HOME_PAGE
from business_meal.addonsapp.model_mixins import ContactUsMixin
from business_meal.services.helpers import file_upload


class SiteConfiguration(SingletonModel):
    def __str__(self):
        return "Site Configuration"

    class Meta:
        verbose_name = "Site Configuration"


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class AbstractSection(models.Model):
    title = models.TextField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    button_text = models.TextField(null=True, blank=True)
    button_hex_color = models.CharField(
        max_length=255, null=True, blank=True, help_text=_("color of button")
    )
    button_text_color = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text=_("color of text inside button"),
    )
    button_url = models.TextField(null=True, blank=True)
    button_float = models.TextField(
        choices=[("right", "right"), ("left", "left"), ("middle", "middle")],
        null=True,
        blank=True,
    )
    color = models.CharField(
        max_length=255, null=True, blank=True, help_text=_("section color")
    )
    hidden = models.BooleanField(default=False)

    class Meta:
        abstract = True


# PageSection


class PageSection(models.Model):
    PAGE_OPTIONS = ((HOME_PAGE, _("home")),)
    page_type = models.CharField(
        _("Page"), max_length=50, choices=PAGE_OPTIONS, default=HOME_PAGE
    )
    section_number = models.IntegerField(default=1)
    is_slider = models.BooleanField(
        _("Is slider"),
        help_text="if enabled, you should add slider pictures.",
        default=False,
    )

    class Meta:
        ordering = ["-section_number"]
        unique_together = (("page_type", "section_number"),)


class SliderPicture(AbstractSection):
    picture = models.ImageField(upload_to=partial(file_upload, "slider_pictures"))
    order_in_front = models.IntegerField(default=0)
    page_section = models.ForeignKey(
        "PageSection", verbose_name=_("Page Section"), on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ["-order_in_front"]


class SectionContent(AbstractSection):
    page_section = models.ForeignKey(
        "PageSection", on_delete=models.CASCADE, blank=True, null=True
    )
    picture = models.ImageField(
        upload_to=partial(file_upload, "section_content"), blank=True, null=True
    )
    url = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}"


# Contact Us


class ContactUs(ContactUsMixin, models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=12)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    class Meta:
        verbose_name = "Contact us"
        verbose_name_plural = "Contact Us"

    def __str__(self):
        return f"{self.name}"


class Ads(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="media/")
    description = models.CharField(max_length=50)
    link = models.URLField(max_length=500)

    def __str__(self):
        return self.name


class TermsAndConditions(models.Model):
    text = models.TextField()


class About(models.Model):
    text = models.TextField()
    instagram = models.URLField(max_length=500)
    twitter = models.URLField(max_length=500)
    facebook = models.URLField(max_length=500)
    snapchat = models.URLField(max_length=500)
    whatsapp = models.CharField(max_length=500)
