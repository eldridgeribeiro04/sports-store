from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartViewSet, CartItemViewSet

router = DefaultRouter()
router.register(r'carts', CartViewSet)
router.register(r'carts/(?P<cart_pk>\d+)/items', CartItemViewSet, basename='cart-item')

urlpatterns = [
    path('', include(router.urls)),
]