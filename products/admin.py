from django.contrib import admin
from .models import Product, Category, ProductSize

class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'category', 'price', 'rating', 'image')
    inlines = [ProductSizeInline]  # allows adding sizes in the same form

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductSize)