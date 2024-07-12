from django.db import models
from accounts.models import MyUser
from base.models import Product

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def __str__(self):
        return f"Cart for user {self.user}"
            
    def add_item(self, product, quantity):
        cart_item, created = CartItem.objects.get_or_create(cart=self, product=product)
        if created:
            cart_item.quantity = quantity
        else:
            cart_item.quantity += quantity
        cart_item.save()
        self.update_total_price()
        
    def update_total_price(self):
        self.total_price = sum(item.get_total_price() for item in self.items.all())
        self.save()
    
    def clear_cart(self):
        self.items.all().delete()
        self.update_total_price()
        

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.product} in cart {self.cart}"
    
    def get_total_price(self):
        return self.product.price * self.quantity
    
    def remove_item(self):
        self.quantity -= 1
        if self.quantity <= 0:
            self.delete()
        else:
            self.save()
        self.cart.update_total_price()
        
    