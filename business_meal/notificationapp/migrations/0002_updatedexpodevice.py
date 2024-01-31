# Generated by Django 4.1.1 on 2024-01-31 00:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "bit68_notifications",
            "0008_auto_20220704_2327",
        ),
        ("notificationapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UpdatedExpoDevice",
            fields=[
                (
                    "expodevice_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="bit68_notifications.expodevice",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[("driver", "driver"), ("customer", "customer")],
                        max_length=50,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("bit68_notifications.expodevice",),
        ),
    ]
