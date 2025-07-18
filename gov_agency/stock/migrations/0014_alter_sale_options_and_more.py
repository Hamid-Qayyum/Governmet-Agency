# Generated by Django 4.2.21 on 2025-06-19 18:57

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0013_alter_sale_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sale',
            options={'ordering': ['-sale_time'], 'verbose_name': 'Sale Record', 'verbose_name_plural': 'Sale Records'},
        ),
        migrations.RenameField(
            model_name='sale',
            old_name='total_cost_dispatch',
            new_name='total_cost',
        ),
        migrations.RenameField(
            model_name='sale',
            old_name='total_revenue_dispatch',
            new_name='total_revenue',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='assigned_vehicle',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='customer_name_manual',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='customer_shop',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='needs_vehicle',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='payment_type',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='quantity_sold_decimal',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='returned_stock_decimal',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='status',
        ),
        migrations.AddField(
            model_name='sale',
            name='name_of_customer',
            field=models.CharField(default='Not Provided', max_length=100),
        ),
        migrations.AddField(
            model_name='sale',
            name='quantity_items_sold',
            field=models.DecimalField(decimal_places=1, default=0.0, help_text="Quantity sold in 'master_unit.item' format (e.g., 1.1 for 1 carton and 1 item).", max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.1'))]),
        ),
        migrations.AlterField(
            model_name='sale',
            name='selling_price_per_item',
            field=models.DecimalField(decimal_places=2, help_text='The price each individual item was sold to the customer for.', max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
    ]
