from django.contrib import admin
from .models import Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_at', 'price', 'availability')
    list_filter = ('status', 'created_at', 'availability')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    ordering = ('status', 'created_at')