# Generated by Django 5.0 on 2024-02-23 22:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("generatorApp", "0002_alter_schedulelist_created_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="schedulelist",
            name="created_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 2, 23, 22, 17, 17, 811231, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
