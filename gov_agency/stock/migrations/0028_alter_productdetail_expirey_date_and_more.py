# Generated by Django 4.2.21 on 2025-07-07 19:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0027_salestransactionitem_discount_percentage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetail',
            name='expirey_date',
            field=models.DateField(default=datetime.date(2025, 8, 7)),
        ),
        migrations.AlterField(
            model_name='salestransactionitem',
            name='product_detail_snapshot',
            field=models.ForeignKey(help_text='The specific product batch (product name, expiry, etc.) sold.', on_delete=django.db.models.deletion.PROTECT, to='stock.productdetail'),
        ),
    ]
