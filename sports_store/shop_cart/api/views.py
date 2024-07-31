from rest_framework.views import APIView
from rest_framework import generics, status

from rest_framework.response import Response

from shop_cart.models import Cart, CartItem
from base.models import Product
from shop_cart.api.serializers import *

from django.shortcuts import get_object_or_404


class GetCartView(APIView):
    
    def get_cart(self, request, *args, **kwargs):
        user = request.user
        
        if user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=user)
        else:
            cart_id = request.session.get('cart_id')
            if cart_id:
                cart = Cart.objects.get(id=cart_id)
            else:
                cart = Cart.objects.create(user=None)
                request.session['cart_id'] = cart.id
        return cart        
        
    def get(self, request, *args, **kwargs):
        cart = self.get_cart(request)
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class CartView(GetCartView):
    
    def post(self, request, product_id, *args, **kwargs):
        cart = self.get_cart(request)
        product = get_object_or_404(Product, pk=product_id)
        quantity = request.data.get('quantity', 1)
        
        if not product_id or not quantity:
            return Response('Invalid request data', status=status.HTTP_400_BAD_REQUEST)        
        
        if product.quantity > 0:
            cart.add_item(product, quantity)
            product.quantity -= quantity
            product.save()
         
        # cart.update_total_price()
        
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def delete(self, request, product_id):
        cart = self.get_cart(request)
        cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)        
        cart_item.remove_item()
        
        return Response(status=status.HTTP_200_OK)
    

class ClearCart(GetCartView):
    
    def post(self, request):
        cart = self.get_cart(request)
        cart.clear_cart()
        
        return Response(status=status.HTTP_200_OK)
    