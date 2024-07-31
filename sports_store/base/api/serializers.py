from rest_framework import serializers

from base.models import *

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        

class ProductSerializer(serializers.ModelSerializer):
    # brand = BrandSerializer(read_only=True)
    # category = CategorySerializer(read_only=True)
    
    class Meta:
        model = Product
        fields = ['id', 'brand', 'category', 'product_name', 'price', 'quantity']
        depth = 1
        

class AddProductQuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['quantity']