# Generated by Django 4.2.1 on 2023-11-07 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_productimages_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='mfd',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_life',
            field=models.CharField(blank=True, default='10', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.CharField(blank=True, default='Homemade', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='stock_count',
            field=models.CharField(blank=True, default='10', max_length=100, null=True),
        ),
    ]
