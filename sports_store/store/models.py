from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    

class Item(models.Model):
    gender_choices = {
        ('male', 'Male'),
        ('female', 'Female'),
        ('unisex', 'Unisex'),
    }
    
    size_choices = {
        ('xs', 'XS'),
        ('s', 'S'),
        ('m', 'M'),
        ('l', 'L'),
        ('xl', 'XL'),
        ('xxl', 'XXL'),
        ('xxxl', 'XXXL'),
        ('3xl', '3XL'),
        ('4xl', '4XL')
    }
    
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    description = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    
    gender = models.CharField(max_length=255, choices=gender_choices)
    size = models.CharField(max_length=255, choices=size_choices)
    
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    
    def __str__(self):
        return self.name
    
    class Meta:
        unique_together = ('name', 'brand', 'category')