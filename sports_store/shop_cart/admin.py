from django.contrib import admin
from shop_cart.models import *
# Register your models here.

admin.site.register(Cart)
admin.site.register(CartItem)