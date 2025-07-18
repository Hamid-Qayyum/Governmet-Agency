# Generated by Django 4.2.21 on 2025-07-05 09:16

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_rename_net_amount_dailysummary_cash_given_as_credit_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailysummary',
            name='cash_given_as_credit',
        ),
        migrations.RemoveField(
            model_name='dailysummary',
            name='cash_received_from_credit',
        ),
        migrations.RemoveField(
            model_name='dailysummary',
            name='net_cash_flow',
        ),
        migrations.AddField(
            model_name='dailysummary',
            name='net_cash_in_hand',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), help_text='The final net cash flow for the day.', max_digits=14),
        ),
        migrations.AddField(
            model_name='dailysummary',
            name='total_cash_received',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), help_text='Cash received from paying off past credit sales.', max_digits=14),
        ),
        migrations.AlterField(
            model_name='dailysummary',
            name='credit_sales_today',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), help_text='Value of ONLY credit sales made today.', max_digits=14),
        ),
        migrations.AlterField(
            model_name='dailysummary',
            name='total_expense',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), help_text='Total cash paid out for expenses.', max_digits=14),
        ),
    ]
