# Generated by Django 5.1.2 on 2024-11-04 17:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productmodel",
            name="date_of_pub",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 11, 4, 17, 54, 17, 296758)
            ),
        ),
    ]