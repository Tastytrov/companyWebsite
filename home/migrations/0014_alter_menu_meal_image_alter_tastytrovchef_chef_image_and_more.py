# Generated by Django 4.2.2 on 2023-07-09 22:38

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_gallery_file_alter_gallery_file_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='meal_image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='tastytrovchef',
            name='chef_image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='star_rating',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='testimonial',
            field=models.TextField(),
        ),
    ]
