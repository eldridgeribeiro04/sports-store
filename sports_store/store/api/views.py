from store.models import Item
from store.api.serializers import ItemSerializer

from rest_framework import views
from rest_framework import viewsets, status, generics

from rest_framework.response import Response

class ItemViewMVS(generics.ListAPIView):
    
    serializer_class = ItemSerializer
    
    def get_queryset(self):
        return super().get_queryset()
        