# Generated by Django 4.0.2 on 2022-06-03 04:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainpage',
            name='title',
            field=models.TextField(default=datetime.datetime(2022, 6, 3, 4, 33, 13, 481929, tzinfo=utc), verbose_name='title'),
            preserve_default=False,
        ),
    ]
