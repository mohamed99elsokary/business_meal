# Generated by Django 4.1.1 on 2023-11-02 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hotel_app", "0006_hallavailabletime_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="hall",
            name="name_ar",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="hall",
            name="name_en",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="hotel",
            name="address_ar",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="hotel",
            name="address_en",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="hotel",
            name="name_ar",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="hotel",
            name="name_en",
            field=models.CharField(max_length=50, null=True),
        ),
    ]
