from django.contrib import admin
from .models import SuccessStory

@admin.register(SuccessStory)
class SuccessStoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'content')
    readonly_fields = ('created_at',)
