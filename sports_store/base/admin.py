from django.contrib import admin
from base.models import Brand, Category, Product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category', 'price', 'size', 'quantity')
    list_filter = ('product_name', 'category', 'quantity')
    search_fields = ('product_name', 'category__name', 'price', 'size')
    

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)