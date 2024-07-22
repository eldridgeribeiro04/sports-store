import django_filters 

from base.models import Product, Brand

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['brand', 'product_name']
        
        
class BrandFilter(django_filters.FilterSet):
    class Meta:
        model = Brand
        fields = '__all__'