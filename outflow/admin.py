from django.contrib import admin
from . import models

class OutflowAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'selling_price',
                    'description', 'created_at', 'updated_at',]
    list_filter = ['product', 'created_at',]
    search_fields = ['product__title', 'created_at',]
    list_per_page = 10

admin.site.register(models.Outflow, OutflowAdmin)