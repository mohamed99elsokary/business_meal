# Generated by Django 4.1.1 on 2023-10-31 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("openbuffet_app", "0002_openbuffetpackage_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="openbuffetpackage",
            name="description_ar",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="openbuffetpackage",
            name="description_en",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="openbuffetpackageoptions",
            name="option_ar",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="openbuffetpackageoptions",
            name="option_en",
            field=models.CharField(max_length=50, null=True),
        ),
    ]
