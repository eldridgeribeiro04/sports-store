from django.db import models

# Create your models here.

class Brand(models.Model):
    brand_name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.brand_name
    

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.category_name
    

class Product(models.Model):
    
    SIZE_CHOICES = [
        ('Extra Small', 'XS'),
        ('Small', 'S'),
        ('Medium', 'M'),
        ('Large', 'L'),
        ('Extra Large', 'XL'),
    ]
    
    product_name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, default=None, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=100, choices=SIZE_CHOICES)
    quantity = models.BigIntegerField(default=1, null=True)
    
    def __str__(self):
        return self.product_name
    
            
    
