# Generated by Django 4.2.21 on 2025-07-10 07:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0032_alter_productdetail_expirey_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetail',
            name='expirey_date',
            field=models.DateField(default=datetime.date(2025, 8, 9)),
        ),
    ]
