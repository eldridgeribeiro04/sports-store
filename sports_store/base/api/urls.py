from django.urls import path

from base.api import views

app_name = 'base'

urlpatterns = [
    # Brand
    path('brand/', views.BrandListView.as_view(), name='brandlist'),
    path('brand/<int:pk>/', views.BrandDetailView.as_view(), name='branddetail'),
    
    # Category
    path('category/', views.CategoryListView.as_view(), name='categorylist'),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name='categorydetail'),
    
    # Product
    path('product/', views.ProductListView.as_view(), name='productlist'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='productdetail'),
    
    # Increase quantity
    path('product/<int:pk>/increase_quantity/', views.AddProductQuantityView.as_view(), name='increase_quantity'),
]
