# Generated by Django 4.1.2 on 2022-10-12 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataAnalytics', '0007_customeraquisition'),
    ]

    operations = [
        migrations.CreateModel(
            name='netProfitMargin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profit', models.FloatField()),
                ('sales', models.FloatField()),
            ],
        ),
    ]
