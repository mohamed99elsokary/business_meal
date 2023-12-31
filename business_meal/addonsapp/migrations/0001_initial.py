# Generated by Django 4.1.1 on 2023-07-03 21:15

import business_meal.addonsapp.model_mixins
import business_meal.services.helpers
from django.db import migrations, models
import django.db.models.deletion
import functools


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ContactUs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=255)),
                ("phone_number", models.CharField(max_length=12)),
                ("subject", models.CharField(max_length=255)),
                ("message", models.TextField()),
            ],
            options={
                "verbose_name": "Contact us",
                "verbose_name_plural": "Contact Us",
            },
            bases=(business_meal.addonsapp.model_mixins.ContactUsMixin, models.Model),
        ),
        migrations.CreateModel(
            name="PageSection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "page_type",
                    models.CharField(
                        choices=[("home", "home")],
                        default="home",
                        max_length=50,
                        verbose_name="Page",
                    ),
                ),
                ("section_number", models.IntegerField(default=1)),
                (
                    "is_slider",
                    models.BooleanField(
                        default=False,
                        help_text="if enabled, you should add slider pictures.",
                        verbose_name="Is slider",
                    ),
                ),
            ],
            options={
                "ordering": ["-section_number"],
                "unique_together": {("page_type", "section_number")},
            },
        ),
        migrations.CreateModel(
            name="SiteConfiguration",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "verbose_name": "Site Configuration",
            },
        ),
        migrations.CreateModel(
            name="SliderPicture",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.TextField(blank=True, null=True)),
                ("text", models.TextField(blank=True, null=True)),
                ("button_text", models.TextField(blank=True, null=True)),
                (
                    "button_hex_color",
                    models.CharField(
                        blank=True,
                        help_text="color of button",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "button_text_color",
                    models.CharField(
                        blank=True,
                        help_text="color of text inside button",
                        max_length=255,
                        null=True,
                    ),
                ),
                ("button_url", models.TextField(blank=True, null=True)),
                (
                    "button_float",
                    models.TextField(
                        blank=True,
                        choices=[
                            ("right", "right"),
                            ("left", "left"),
                            ("middle", "middle"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "color",
                    models.CharField(
                        blank=True, help_text="section color", max_length=255, null=True
                    ),
                ),
                ("hidden", models.BooleanField(default=False)),
                (
                    "picture",
                    models.ImageField(
                        upload_to=functools.partial(
                            business_meal.services.helpers.file_upload,
                            *("slider_pictures",),
                            **{}
                        )
                    ),
                ),
                ("order_in_front", models.IntegerField(default=0)),
                (
                    "page_section",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="addonsapp.pagesection",
                        verbose_name="Page Section",
                    ),
                ),
            ],
            options={
                "ordering": ["-order_in_front"],
            },
        ),
        migrations.CreateModel(
            name="SectionContent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.TextField(blank=True, null=True)),
                ("text", models.TextField(blank=True, null=True)),
                ("button_text", models.TextField(blank=True, null=True)),
                (
                    "button_hex_color",
                    models.CharField(
                        blank=True,
                        help_text="color of button",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "button_text_color",
                    models.CharField(
                        blank=True,
                        help_text="color of text inside button",
                        max_length=255,
                        null=True,
                    ),
                ),
                ("button_url", models.TextField(blank=True, null=True)),
                (
                    "button_float",
                    models.TextField(
                        blank=True,
                        choices=[
                            ("right", "right"),
                            ("left", "left"),
                            ("middle", "middle"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "color",
                    models.CharField(
                        blank=True, help_text="section color", max_length=255, null=True
                    ),
                ),
                ("hidden", models.BooleanField(default=False)),
                (
                    "picture",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=functools.partial(
                            business_meal.services.helpers.file_upload,
                            *("section_content",),
                            **{}
                        ),
                    ),
                ),
                ("url", models.TextField(blank=True, null=True)),
                (
                    "page_section",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="addonsapp.pagesection",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
