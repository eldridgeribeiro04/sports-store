from django.shortcuts import get_object_or_404

from shop_cart.api.serializers import *
from shop_cart.models import *

from rest_framework import status, mixins, generics, viewsets

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(user=user)
    
    def add_item(self, request, pk=None):
        cart = self.get_object()
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)
        
        try:
            product = Product.objects.get(id=product_id)
            cart.add_item(product, quantity)
            cart_serializer = CartSerializer(cart)
            return Response(cart_serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        
    @action(detail=True, methods=['post'])
    def remove_item(self, request, pk=None):
        cart = self.get_object()
        product_id = request.data.get('product_id')
        
        try:
            product = Product.objects.get(id=product_id)
            cart.remove_item(product)
            cart_serializer = CartSerializer(cart)
            return Response(cart_serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        
    @action(detail=True, methods=['post'])
    def clear(self, request, pk=None):
        cart = self.get_object()
        cart.clear_cart() 
        cart_serializer = CartSerializer(cart)
        return Response(cart_serializer.data, status=status.HTTP_200_OK)
    
    
class CartItemSerializer(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    
    def get_queryset(self):
        cart_id = self.kwargs.get('cart_pk')
        return CartItem.objects.filter(cart_id=cart_id)
    
    def perform_create(self, serializer):
        cart_id = self.kwargs.get('cart_pk')
        serializer.save(cart_id=cart_id)