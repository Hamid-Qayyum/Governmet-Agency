# Generated by Django 4.2.21 on 2025-07-07 23:09

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0029_remove_salestransactionitem_discount_percentage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salestransactionitem',
            name='product_detail_snapshot',
            field=models.ForeignKey(help_text='The specific product batch sold.', on_delete=django.db.models.deletion.PROTECT, to='stock.productdetail'),
        ),
        migrations.AlterField(
            model_name='salestransactionitem',
            name='returned_quantity_decimal',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))]),
        ),
    ]
