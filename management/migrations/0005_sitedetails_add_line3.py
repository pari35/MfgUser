# Generated by Django 4.0 on 2022-02-07 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_sitedetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitedetails',
            name='add_line3',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
