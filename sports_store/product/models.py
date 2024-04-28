from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='images/logos/', blank=True, null=True)

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"
        ordering = ['name']

    def __str__(self):
        return self.name
    

class Gender(models.Model):
    gender_type = models.CharField(max_length=255, default='Not assigned')

    class Meta:
        verbose_name = "Gender"
        verbose_name_plural = "Genders"

    def __str__(self):
        return self.gender_type
    

class Category(models.Model):
    category_type = models.CharField(max_length=255)
    brand = models.ManyToManyField(Brand)
    gender = models.ManyToManyField(Gender)

    class Meta:
        ordering = ['category_type']
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        indexes = [
            models.Index(fields=['category_type']),
        ]

    def __str__(self):
        return self.category_type


class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    rating = models.FloatField(default=0.0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    image = models.ImageField(upload_to='images/items', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brands')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
        verbose_name = "Item"
        verbose_name_plural = "Items"
        indexes = [
            models.Index(fields=['brand', 'category'])
        ]

    def __str__(self):
        return self.name
