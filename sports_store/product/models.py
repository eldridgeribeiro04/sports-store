from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='images/logos/', blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    

class Category(models.Model):
    category_type = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.category_type


class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    image = models.ImageField(upload_to='images/items', blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
