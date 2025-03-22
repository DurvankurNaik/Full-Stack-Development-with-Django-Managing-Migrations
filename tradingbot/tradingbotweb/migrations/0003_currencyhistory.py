# Generated by Django 5.1.6 on 2025-03-06 03:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradingbotweb', '0002_auto_20250306_0343'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usd_value', models.DecimalField(decimal_places=6, default=1.0, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('symbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tradingbotweb.currency')),
            ],
        ),
    ]
