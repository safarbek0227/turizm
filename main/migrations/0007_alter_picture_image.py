# Generated by Django 4.0.2 on 2022-06-03 06:13

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_category_slug_alter_category_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=0, size=[283, 183], upload_to=''),
        ),
    ]