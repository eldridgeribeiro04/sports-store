from django.shortcuts import render
from product.models import Brand, Category, Item
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    brands = Brand.objects.all()
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)
    return render(request, 'core/base.html', {
        'brands': brands,
        'categories': categories,
        'items': items
    })