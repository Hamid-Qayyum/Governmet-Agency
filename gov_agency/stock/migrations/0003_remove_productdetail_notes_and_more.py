# Generated by Django 4.2.21 on 2025-06-07 20:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_productdetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productdetail',
            name='notes',
        ),
        migrations.AddField(
            model_name='productdetail',
            name='expirey_date',
            field=models.DateField(default=datetime.date(2025, 7, 8)),
        ),
        migrations.AddField(
            model_name='productdetail',
            name='stock',
            field=models.PositiveIntegerField(default=1, help_text='Enter Stock'),
        ),
        migrations.AlterField(
            model_name='productdetail',
            name='packing_type',
            field=models.CharField(default='Carton', help_text='e.g., Bottle, Box, Carton, PET Jar', max_length=100),
        ),
        migrations.AlterField(
            model_name='productdetail',
            name='unit_of_measure',
            field=models.CharField(default='liter', help_text='e.g., kg, liter, pieces, meters', max_length=50),
        ),
    ]
