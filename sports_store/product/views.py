from typing import Any
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Item, Brand
# from django.views.generic import TemplateView
# Create your views here.


def items(request, brand_id):
    brand = get_object_or_404(Brand, pk=brand_id)
    items = Item.objects.filter(brand=brand)
    return render(request, 'product/items.html', {
        'items': items,
        'brand_item': brand
    })


def item_view(request, item_id):
    single_item = get_object_or_404(Item, pk=item_id)
    return render(request, 'product/single_item.html', {
        'single_item': single_item
    })
