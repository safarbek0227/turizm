# Generated by Django 4.0.2 on 2022-06-03 04:30

import ckeditor.fields
from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=0, size=[1920, 1080], upload_to='MainPage%Y%m', verbose_name='Image')),
                ('content', ckeditor.fields.RichTextField(max_length=250)),
            ],
        ),
    ]