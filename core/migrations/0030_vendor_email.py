# Generated by Django 4.2.6 on 2024-01-20 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_delete_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='email',
            field=models.CharField(default='example@mail.com', max_length=100),
        ),
    ]