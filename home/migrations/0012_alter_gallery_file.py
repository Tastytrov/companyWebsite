# Generated by Django 4.2.2 on 2023-07-09 22:30

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_testimonial_client_social'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='file',
            field=cloudinary.models.CloudinaryField(default='a.png', max_length=255, verbose_name='file'),
        ),
    ]
