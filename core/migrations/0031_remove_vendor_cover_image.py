# Generated by Django 4.2.6 on 2024-01-20 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_vendor_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='cover_image',
        ),
    ]