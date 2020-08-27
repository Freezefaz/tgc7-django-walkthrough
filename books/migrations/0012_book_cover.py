# Generated by Django 2.2.13 on 2020-08-27 07:25

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_book_page_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=cloudinary.models.CloudinaryField(default='', max_length=255),
            preserve_default=False,
        ),
    ]