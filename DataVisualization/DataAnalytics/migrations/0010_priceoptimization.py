# Generated by Django 4.1.2 on 2022-10-13 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataAnalytics', '0009_netprofitmargin_profitmargin1'),
    ]

    operations = [
        migrations.CreateModel(
            name='priceOptimization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priceSell', models.FloatField()),
                ('costMake', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('maxProfit', models.FloatField()),
            ],
        ),
    ]