import stripe

from django.conf import settings
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from shop_cart.models import Cart, CartItem
from shop_cart.api.serializers import CartSerializer
from shop_cart.api.views import GetCartView

from payment.models import Payment

stripe.api_key = settings.STRIPE_SECRET_KEY


class PaymentView(APIView):
    
    def post(self, request, cart_id, *args, **kwargs):
        # cart_id = request.data.get('cart_id')
        cart = get_object_or_404(Cart, pk=cart_id)
        # cart = get_object_or_404(Cart, cart_pk=cart_pk)
        token = request.data.get('stripe_token')
        amount = int(cart.total_price * 100) 
        
        try:
            charge = stripe.Charge.create(
                amount=amount,
                currency='usd',
                source=token,
                description='Payment for cart {}'.format(cart.id),
            )
            
            payment = Payment.objects.create(
                cart=cart,
                amount=amount,
                stripe_charge_id = charge.id
            )
            
            cart.paid = True
            cart.save()
            return Response({'message': 'Payment successful'}, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'Payment failed'}, status=status.HTTP_400_BAD_REQUEST)
