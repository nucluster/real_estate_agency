# Generated by Django 2.2.24 on 2022-01-21 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_auto_20190829_2242'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flat',
            old_name='active',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='flat',
            old_name='rooms_number',
            new_name='number_of_rooms',
        ),
    ]
