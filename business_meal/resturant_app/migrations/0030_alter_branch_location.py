# Generated by Django 4.1.1 on 2023-10-21 09:16

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("resturant_app", "0029_meal_is_top_dish"),
    ]

    operations = [
        migrations.AlterField(
            model_name="branch",
            name="location",
            field=django.contrib.gis.db.models.fields.PointField(
                blank=True, null=True, srid=4326
            ),
        ),
    ]
