# Generated by Django 4.1.1 on 2023-07-26 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resturant_app", "0023_category_image_openbuffetpackage_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="hotel",
            name="cover_photo",
            field=models.ImageField(
                blank=True, default=None, null=True, upload_to="media/"
            ),
        ),
        migrations.AddField(
            model_name="restaurant",
            name="cover_photo",
            field=models.ImageField(
                blank=True, default=None, null=True, upload_to="media/"
            ),
        ),
    ]
