from django.urls import path
from base import views

app_name = 'base'

urlpatterns = [
    path('home/', views.home, name='home'),
    
    path('add_brand', views.add_brand, name='add_brand'),
    path('add_category', views.add_category, name='add_category'),
    path('add_product', views.add_product, name='add_product'),
    
    path('<str:brand_name>/', views.filter_by_brand, name='brand'),
    
    path('<str:brand_name>/<int:product_id>/', views.single_product_view, name='product'),
    path('add_quantity/<int:product_id>', views.increase_quantity, name='add_quantity'),
]