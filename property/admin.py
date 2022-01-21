from django.contrib import admin

from .models import Flat


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner', 'construction_year')
    list_display = ('town', 'address', 'price', 'is_new_building',
                    'construction_year', 'owners_phonenumber')
    list_editable = ('is_new_building',)
    list_filter = ('is_new_building', 'number_of_rooms', 'has_balcony')