from django.contrib import admin
from . import models

class InflowAdmin(admin.ModelAdmin):
    list_display = ['supplier', 'product', 'quantity', 'cost_price',
                    'description', 'created_at', 'updated_at',]
    search_fields = ['product__title', 'supplier__name',]
    list_per_page = 10

admin.site.register(models.Inflow, InflowAdmin)
