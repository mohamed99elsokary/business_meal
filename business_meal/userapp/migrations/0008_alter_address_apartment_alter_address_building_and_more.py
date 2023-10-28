# Generated by Django 4.1.1 on 2023-10-28 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("userapp", "0007_address_description_address_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="address",
            name="apartment",
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="address",
            name="building",
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="address",
            name="description",
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name="address",
            name="floor",
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="address",
            name="is_default",
            field=models.BooleanField(
                blank=True, default=False, null=True, verbose_name="Is default"
            ),
        ),
        migrations.AlterField(
            model_name="address",
            name="postal_code",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=100,
                null=True,
                verbose_name="Postal code",
            ),
        ),
        migrations.AlterField(
            model_name="address",
            name="street",
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="address",
            name="user",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="User",
            ),
        ),
    ]
