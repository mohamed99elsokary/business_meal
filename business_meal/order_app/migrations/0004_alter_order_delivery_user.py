# Generated by Django 4.1.1 on 2023-09-22 20:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("order_app", "0003_alter_order_delivered_time_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="delivery_user",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="delivery_user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]