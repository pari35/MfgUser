# Generated by Django 4.0.1 on 2022-02-03 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProfilePic',
        ),
        migrations.AddField(
            model_name='adduser',
            name='profile_pic',
            field=models.ImageField(default='', upload_to='static/images'),
        ),
    ]
