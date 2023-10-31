# Generated by Django 4.1.1 on 2023-10-31 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hotel_app", "0004_hallavailabletime"),
    ]

    operations = [
        migrations.AddField(
            model_name="hall",
            name="description_ar",
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name="hall",
            name="description_en",
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name="halloptions",
            name="option_ar",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="halloptions",
            name="option_en",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="hotel",
            name="description_ar",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="hotel",
            name="description_en",
            field=models.TextField(null=True),
        ),
    ]
