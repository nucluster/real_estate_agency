from django.contrib import admin

from .models import Flat, Complaint, Owner


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner', 'construction_year')
    list_display = ('town', 'address', 'price', 'is_new_building',
                    'construction_year', 'owners_phonenumber',
                    'owner_pure_phone')
    list_editable = ('is_new_building',)
    list_filter = ('is_new_building', 'number_of_rooms', 'has_balcony')
    raw_id_fields = ('likes',)


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('author', 'flat')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)

