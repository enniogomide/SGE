from django.contrib import admin
from . import models

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'brand', 'category',
                    'serie_number', 'cost_price',
                    'selling_price', 'quantity',
                    'description', 'created_at', 'updated_at',]
    list_filter = ['title', 'brand', 'category',]
    search_fields = ['title',]
    list_per_page = 10

admin.site.register(models.Product, ProductAdmin)