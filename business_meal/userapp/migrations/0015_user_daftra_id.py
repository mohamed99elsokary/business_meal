# Generated by Django 4.1.1 on 2024-03-13 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userapp", "0014_user_loyalty_points"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="daftra_id",
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
