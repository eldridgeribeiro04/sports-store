from rest_framework import serializers
from .models import Todo

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        # fields = ('id', 'title', 'description', 'completed')