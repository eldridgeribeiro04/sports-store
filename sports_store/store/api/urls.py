from django.urls import path
from store.api import views

urlpatterns = [
    # Item URL pattern
    path('items/', views.ItemViewMVS.as_view(), name='items'),
    path('items/<int:pk>/', views.ItemDetailViewMVS.as_view(), name='single_item'),
    
    # Brand URL pattern
    path('brands/', views.BrandViewMVS.as_view(), name='brand'),
    path('brands/<int:pk>/', views.BrandDetailViewMVS.as_view(), name='single_brand'),
    
    # Category URL pattern
    path('category/', views.CategoryViewMVS.as_view(), name='category'),
    path('category/<int:pk>/', views.CategoryDetailViewMVS.as_view(), name='single_category'),
]