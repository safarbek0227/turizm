# Generated by Django 4.0.2 on 2022-06-03 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_mainpage_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainpage',
            name='img',
            field=models.ImageField(upload_to=''),
        ),
    ]
