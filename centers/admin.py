from django.contrib import admin
from .models import Center

@admin.register(Center)
class CenterAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'city', 'contact_number', 'latitude', 'longitude')
    
    list_filter = ('city',)
    
    search_fields = ('name', 'address', 'city')
    
    