from django.contrib import admin
from .models import Center

@admin.register(Center)
class CenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'center_type', 'city', 'contact_number')
    list_filter = ('center_type', 'city')
    search_fields = ('name', 'address', 'city')
    readonly_fields = ('latitude', 'longitude')
