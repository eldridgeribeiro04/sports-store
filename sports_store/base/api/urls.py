from django.urls import path
from base.api import views

app_name = 'base'

urlpatterns = [
    path('brand/', views.BrandAPIView.as_view(), name='brand'),
    path('brand/<int:pk>/', views.BrandDetailAPIView.as_view(), name='brand_detail'),
    
    path('category/', views.CategoryAPIView.as_view(), name='category'),
    path('category/<int:pk>/', views.CategoryDetailAPIView.as_view(), name='category_detail'),
    
    path('product/', views.ProductAPIView.as_view(), name='product'),
    path('product/<int:pk>/', views.ProductDetailAPIView.as_view(), name='product_detail'),
    
    path('add/<int:pk>/', views.IncreaseQuantityAPIView.as_view(), name='increase_quantity'),

]