from django.contrib import admin
from . import models

class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at', 'updated_at', 'is_active',]
    list_filter = ['name', 'created_at', 'updated_at', 'is_active',]
    search_fields = ['name',]
    list_per_page = 10

admin.site.register(models.Brand, BrandAdmin)

