# Generated by Django 5.1.2 on 2024-11-06 07:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0012_alter_productmodel_date_of_pub"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productmodel",
            name="date_of_pub",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 11, 6, 7, 56, 20, 630638)
            ),
        ),
    ]
