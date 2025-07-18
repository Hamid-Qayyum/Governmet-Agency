# Generated by Django 4.2.21 on 2025-07-05 08:53

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_dailysummary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dailysummary',
            old_name='net_amount',
            new_name='cash_given_as_credit',
        ),
        migrations.RenameField(
            model_name='dailysummary',
            old_name='total_cash_received',
            new_name='cash_received_from_credit',
        ),
        migrations.AddField(
            model_name='dailysummary',
            name='credit_sales_today',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=14),
        ),
        migrations.AddField(
            model_name='dailysummary',
            name='net_cash_flow',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=14),
        ),
    ]
