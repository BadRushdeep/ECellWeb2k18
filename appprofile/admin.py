from django.contrib import admin
from django.db import models
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'user_type', 'contact_no')
    search_fields = ('id', 'user__first_name', 'user__last_name', 'user_type', 'contact_no')
    list_filter = ('user_type',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'modified_at')

admin.site.register(Profile, ProfileAdmin)