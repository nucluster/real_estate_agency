# Generated by Django 2.2.24 on 2022-01-22 12:01

from django.db import migrations
import phonenumbers


def fill_pure_phone_numbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        owner_pure_phone = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        if phonenumbers.is_valid_number(owner_pure_phone):
            flat.owner_pure_phone = phonenumbers.format_number(
                         owner_pure_phone, phonenumbers.PhoneNumberFormat.E164)
            flat.save()



class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_auto_20220122_1627'),
    ]

    operations = [
        migrations.RunPython(fill_pure_phone_numbers),
    ]