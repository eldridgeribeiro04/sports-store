from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status, generics

from base.api.serializers import *

from django.shortcuts import get_object_or_404


# class BrandListView(APIView):
    
    # def get(self, request):
    #     # Implement logic to retrieve all brands
    #     brands = Brand.objects.all()
    #     serializer = BrandSerializer(brands, many=True)
    #     return Response(serializer.data)
    
    # def post(self, request):
    #     # Implement logic to create a new brand
    #     serializer = BrandSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Brand
class BrandListView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
        
    
class BrandDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    
    
# Category 
class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    
# Product
class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class AddProductQuantityView(APIView):
    
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        serializer = AddProductQuantitySerializer(data=request.data)
        if serializer.is_valid():
            quantity = serializer.validated_data['quantity']
            product.quantity += quantity
            product.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)