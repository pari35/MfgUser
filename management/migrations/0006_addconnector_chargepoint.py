# Generated by Django 4.0 on 2022-02-07 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_sitedetails_add_line3'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddConnector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('connector_type', models.CharField(max_length=20)),
                ('connector_id', models.CharField(max_length=20)),
                ('connector_name', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
                ('plug_type_name', models.CharField(max_length=20)),
                ('max_charge_rate', models.CharField(max_length=20)),
                ('tariff_amount', models.CharField(max_length=20)),
                ('tariff_currency', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ChargePoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charge_id', models.CharField(max_length=20)),
                ('charge_name', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
                ('back_office', models.CharField(max_length=20)),
                ('device_id', models.IntegerField()),
            ],
        ),
    ]