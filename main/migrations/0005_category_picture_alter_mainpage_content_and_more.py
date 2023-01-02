# Generated by Django 4.0.2 on 2022-06-03 05:28

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_mainpage_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='mainpage',
            name='content',
            field=ckeditor.fields.RichTextField(max_length=305),
        ),
        migrations.AlterField(
            model_name='mainpage',
            name='img',
            field=models.ImageField(upload_to='book_images%Y%m'),
        ),
        migrations.CreateModel(
            name='TravelTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('small_content', models.CharField(max_length=250)),
                ('content', ckeditor.fields.RichTextField()),
                ('travel_hours', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
                ('img', models.ManyToManyField(to='main.Picture')),
            ],
        ),
    ]