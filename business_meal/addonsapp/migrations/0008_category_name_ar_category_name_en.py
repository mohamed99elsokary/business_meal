# Generated by Django 4.1.1 on 2023-10-31 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("addonsapp", "0007_privacypolicy"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="name_ar",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="category",
            name="name_en",
            field=models.CharField(max_length=50, null=True),
        ),
    ]
