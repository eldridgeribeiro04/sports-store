from store.models import Item, Brand, Category
from store.api.serializers import ItemSerializer, BrandSerializer, CategorySerializer

from rest_framework import views
from rest_framework import viewsets, status, generics

from rest_framework.response import Response


# First get a whole list of products.
# Then get individual item
# Then add CRUD which will only be accessed by admin


# Item Views
class ItemViewMVS(generics.ListAPIView):
    
    serializer_class = ItemSerializer
    
    def get_queryset(self):
        return Item.objects.all()
    
    def post(self, request):
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class ItemDetailViewMVS(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = ItemSerializer
    
    def get_queryset(self):
        return Item.objects.all()
    
# Brand Views

class BrandViewMVS(generics.ListAPIView):
    
    serializer_class = BrandSerializer
    
    def get_queryset(self):
        return Brand.objects.all()
    
    def post(self, request):
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class BrandDetailViewMVS(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = BrandSerializer
    
    def get_queryset(self):
        return Brand.objects.all()
    
    
# Category Views
class CategoryViewMVS(generics.ListAPIView):
    
    serializer_class = CategorySerializer
    
    def get_queryset(self):
        return Category.objects.all()
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class CategoryDetailViewMVS(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = CategorySerializer
    
    def get_queryset(self):
        return Brand.objects.all()