# Generated by Django 4.1.1 on 2023-12-21 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("addonsapp", "0013_siteconfiguration_is_send_msg"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ads",
            name="name",
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name="ads",
            name="name_ar",
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name="ads",
            name="name_en",
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name="category",
            name="name_ar",
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name="category",
            name="name_en",
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name="optionscategory",
            name="name",
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name="optionscategory",
            name="name_ar",
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name="optionscategory",
            name="name_en",
            field=models.CharField(max_length=250, null=True),
        ),
    ]
