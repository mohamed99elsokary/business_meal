# Generated by Django 4.1.1 on 2024-01-31 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("addonsapp", "0015_alter_ads_description_alter_ads_description_ar_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="LoyaltyPointsPromoCode",
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
                ("price", models.IntegerField()),
                ("discount", models.IntegerField()),
                (
                    "image",
                    models.ImageField(
                        blank=True, default=None, null=True, upload_to=""
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, default=None, max_length=50, null=True
                    ),
                ),
            ],
        ),
    ]
