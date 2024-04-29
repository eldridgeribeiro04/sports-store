from typing import Any
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Item, Brand, Category
# from django.views.generic import TemplateView
# Create your views here.


def items(request, brand_id):
    category = Category.objects.all()
    brand = get_object_or_404(Brand, pk=brand_id)
    items = Item.objects.filter(brand=brand)

    filter_by_category = request.GET.get('filter_by_category')

    if filter_by_category:
        items = items.filter(category_id=filter_by_category)

    return render(request ,'product/items.html', {
        'brand': brand,
        'items': items,
        'category':category,
    })

def item_view(request, item_id):
    single_item = get_object_or_404(Item, pk=item_id)
    return render(request, 'product/single_item.html', {
        'single_item': single_item
    })


def category_view(request):
    categories = Category.objects.all()
    return render(request, 'product/category.html', {
        'categories': categories,
        })
