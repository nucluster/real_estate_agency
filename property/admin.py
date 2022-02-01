from django.contrib import admin

from .models import Flat, Complaint, Owner


class FlatInline(admin.TabularInline):
    model = Flat.owners.through
    raw_id_fields = ('flat', 'owner')


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'construction_year')
    list_display = ('id', 'town', 'address', 'price', 'is_new_building',
                    'construction_year')
    list_editable = ('is_new_building',)
    list_filter = ('is_new_building', 'number_of_rooms', 'has_balcony')
    raw_id_fields = ('likes',)
    list_display_links = ('id',)
    readonly_fields = ('created_at',)
    ordering = ('id',)
    inlines = [FlatInline,]



@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('author', 'flat')



@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
    search_fields = ('fio',)
    list_display = ('id', 'fio', 'pure_phone_number')
    list_display_links = ('fio',)
    ordering = ('-id',)
    inlines = [FlatInline,]
    exclude = ('flats',)

