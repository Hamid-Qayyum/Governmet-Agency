# Generated by Django 4.2.21 on 2025-06-09 07:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_alter_productdetail_stock'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='productdetail',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='productdetail',
            name='expirey_date',
            field=models.DateField(default=datetime.date(2025, 7, 9)),
        ),
        migrations.AlterUniqueTogether(
            name='productdetail',
            unique_together={('product_base', 'packing_type', 'quantity_in_packing', 'unit_of_measure', 'expirey_date', 'stock')},
        ),
    ]
