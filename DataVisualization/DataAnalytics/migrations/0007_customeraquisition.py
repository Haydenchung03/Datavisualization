# Generated by Django 3.2.8 on 2022-09-30 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataAnalytics', '0006_remove_netprofit_netprofit1'),
    ]

    operations = [
        migrations.CreateModel(
            name='customerAquisition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marketing', models.FloatField()),
                ('newCustomer', models.IntegerField()),
            ],
        ),
    ]
