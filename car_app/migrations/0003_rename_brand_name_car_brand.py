# Generated by Django 5.0.6 on 2024-07-27 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0002_car_brand_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='Brand_name',
            new_name='Brand',
        ),
    ]
