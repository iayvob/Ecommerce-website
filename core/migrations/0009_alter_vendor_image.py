# Generated by Django 4.2.1 on 2023-11-05 13:36

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_vendor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='image',
            field=models.ImageField(default='vendor.jpg', upload_to=core.models.user_directory_path),
        ),
    ]
