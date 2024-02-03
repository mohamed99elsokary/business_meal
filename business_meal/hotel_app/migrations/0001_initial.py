# Generated by Django 4.1.1 on 2023-08-15 21:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Hall",
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
                ("min", models.IntegerField(default=0, help_text="number of guests")),
                ("max", models.IntegerField(default=0, help_text="number of guests")),
                ("price", models.IntegerField()),
                ("name", models.CharField(max_length=50)),
                ("description", models.TextField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Hotel",
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
                ("name", models.CharField(max_length=50)),
                (
                    "image",
                    models.ImageField(
                        blank=True, default=None, null=True, upload_to="media/"
                    ),
                ),
                (
                    "cover_photo",
                    models.ImageField(
                        blank=True, default=None, null=True, upload_to="media/"
                    ),
                ),
                ("description", models.TextField()),
                ("address", models.CharField(max_length=50)),
                (
                    "admin",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="HallOptions",
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
                ("option", models.CharField(max_length=50)),
                ("price", models.IntegerField(default=0)),
                (
                    "hall",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="hotel_app.hall"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="HallImages",
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
                ("image", models.ImageField(upload_to="media/")),
                (
                    "hall",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="hotel_app.hall"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="hall",
            name="hotel",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="hotel_app.hotel"
            ),
        ),
    ]