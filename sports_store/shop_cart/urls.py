from django.urls import path
from .views import add_to_cart, cart_detail, remove_from_cart, clear_cart

app_name = 'shop_cart'

urlpatterns = [
    path('cart_detail/', cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/clear/', clear_cart, name='clear_cart'),
]