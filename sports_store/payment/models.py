from django.db import models

from shop_cart.models import Cart

# Create your models here.

class Payment(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    stripe_charge_id = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()
    paid_at = models.DateTimeField(auto_now_add=True)