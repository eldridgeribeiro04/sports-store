from django.shortcuts import render, get_object_or_404, redirect
from shop_cart.models import *
from base.models import Product
from django.contrib.auth.decorators import login_required
# Create your views here.


def get_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        cart_id = request.session.get('cart_id')
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = Cart.objects.create(user=None)
            request.session['cart_id'] = cart.id
    return cart


def cart_detail(request):
    cart = get_cart(request)
    return render(request, 'shop_cart/cart_detail.html', {'cart': cart})


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = get_cart(request)
    
    if product.quantity > 0:
        cart.add_item(product, 1)
        product.quantity -= 1
        product.save()
        return redirect('base:product',brand_name=product.brand.brand_name, product_id=product.id)
    else:
        return redirect('base:product', brand_name=product.brand.brand_name, product_id=product.id)


@login_required
def remove_from_cart(request, product_id):
    cart = get_cart(request)
    print(f"Cart: {cart}")
    print(f"Product ID: {product_id}")
    cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)
    cart_item.remove_item()
    return redirect('shop_cart:cart_detail')

@login_required
def clear_cart(request):
    cart = get_cart(request)
    cart.clear_cart()
    return redirect('cart_detail')

