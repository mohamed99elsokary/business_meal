# Generated by Django 4.1.1 on 2023-10-27 19:57

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("hotel_app", "0002_hotel_rate"),
    ]

    operations = [
        migrations.AddField(
            model_name="hotel",
            name="location",
            field=django.contrib.gis.db.models.fields.PointField(
                blank=True, null=True, srid=4326
            ),
        ),
    ]
