# Generated by Django 5.1.2 on 2024-11-05 09:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0005_alter_productmodel_date_of_pub"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productmodel",
            name="date_of_pub",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 11, 5, 9, 22, 28, 147723)
            ),
        ),
    ]
