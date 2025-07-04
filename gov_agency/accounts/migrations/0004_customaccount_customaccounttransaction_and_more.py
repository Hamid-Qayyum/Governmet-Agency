# Generated by Django 4.2.21 on 2025-07-03 23:36

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_customtransaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='A unique name for this person or entity.', max_length=200)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='custom_accounts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Custom Account',
                'verbose_name_plural': 'Custom Accounts',
                'ordering': ['name'],
                'unique_together': {('user', 'name')},
            },
        ),
        migrations.CreateModel(
            name='CustomAccountTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debit_amount', models.DecimalField(decimal_places=2, default=Decimal('0.00'), help_text='Amount owed TO you by this entity (increases their balance).', max_digits=12)),
                ('credit_amount', models.DecimalField(decimal_places=2, default=Decimal('0.00'), help_text='Amount paid BY you or received FROM this entity (decreases their balance).', max_digits=12)),
                ('notes', models.CharField(blank=True, max_length=255, null=True)),
                ('transaction_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='accounts.customaccount')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Custom Account Transaction',
                'verbose_name_plural': 'Custom Account Transactions',
                'ordering': ['-transaction_date', '-pk'],
            },
        ),
        migrations.DeleteModel(
            name='CustomTransaction',
        ),
    ]
