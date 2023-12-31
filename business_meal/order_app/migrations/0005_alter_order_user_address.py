# Generated by Django 4.1.1 on 2023-09-22 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("userapp", "0005_user_is_new"),
        ("order_app", "0004_alter_order_delivery_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="user_address",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="userapp.address",
            ),
        ),
    ]
