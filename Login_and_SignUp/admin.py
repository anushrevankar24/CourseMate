from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'email', 'id', 'department', 'program_type')

admin.site.register(CustomUser, CustomUserAdmin)


