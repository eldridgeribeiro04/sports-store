from base.models import *
from rest_framework import serializers

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
        fields = '__all__'
        depth = 1
        
        
class IncreaseProductCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['quantity']