# Generated by Django 5.0 on 2024-02-23 20:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("generatorApp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="schedulelist",
            name="created_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 2, 23, 20, 9, 47, 665574, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
