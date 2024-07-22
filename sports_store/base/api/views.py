from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework import status, mixins, generics

from base.models import *
from base.api.serializers import *

from django.http import Http404
from django.shortcuts import get_object_or_404


class BrandAPIView(generics.ListCreateAPIView):
    
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    
    
class BrandDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes  = [IsAdminUser]
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CategoryAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes  = [IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class ProductAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes  = [IsAdminUser]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
class IncreaseQuantityAPIView(APIView):
    
    permission_classes  = [IsAdminUser]
    
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = IncreaseProductCountSerializer(data=request.data)
        if serializer.is_valid():
            quantity = serializer.validated_data['quantity']
            if quantity == None:
                quantity = 0
                product.quantity += quantity
                product.save()
            else:
                product.quantity += quantity
                product.save()
            return Response({
                'product_id': product.id,
                'product_name': product.product_name,
                'brand_name': product.brand.brand_name,
                'quantity': product.quantity,
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    