# Generated by Django 4.2.21 on 2025-07-08 20:23

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0032_alter_productdetail_expirey_date'),
        ('claim', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='claim',
            options={'ordering': ['-claim_date']},
        ),
        migrations.RemoveField(
            model_name='claim',
            name='product_detail',
        ),
        migrations.RemoveField(
            model_name='claim',
            name='quantity_claimed_decimal',
        ),
        migrations.AlterField(
            model_name='claim',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending - Being Built'), ('AWAITING_PROCESSING', 'Awaiting Stock Adjustment'), ('COMPLETED', 'Completed')], default='PENDING', max_length=30),
        ),
        migrations.CreateModel(
            name='ClaimItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_type', models.CharField(choices=[('CLAIMED', 'Item Returned by Customer'), ('EXCHANGED', 'Item Given in Exchange')], max_length=20)),
                ('quantity_decimal', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('cost_price_at_claim', models.DecimalField(decimal_places=2, max_digits=10)),
                ('claim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='claim.claim')),
                ('product_detail', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='claim_items', to='stock.productdetail')),
            ],
        ),
    ]
