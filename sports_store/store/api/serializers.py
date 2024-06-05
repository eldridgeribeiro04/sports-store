# within app imports
from store.models import Category

# rest framework imports
from rest_framework import serializers


class ItemSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    
    class Meta:
        model = Category
        fields = '__all__'