from django.contrib import admin
from .models import Brand, Category, Item, Gender
# Register your models here.

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Gender)
