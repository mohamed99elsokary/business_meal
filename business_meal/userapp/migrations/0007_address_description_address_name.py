# Generated by Django 4.1.1 on 2023-10-22 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userapp", "0006_alter_address_location"),
    ]

    operations = [
        migrations.AddField(
            model_name="address",
            name="description",
            field=models.TextField(default=" "),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="address",
            name="name",
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
