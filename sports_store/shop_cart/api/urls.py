from django.urls import path

from shop_cart.api import views

app_name = 'shop_cart'

urlpatterns = [
    path('get_cart/', views.GetCartView.as_view(), name='cart_detail'),
    path('item/<int:product_id>/', views.CartView.as_view(), name='add_to_cart'),
    path('clear/', views.ClearCart.as_view(), name='clear_cart'),
]