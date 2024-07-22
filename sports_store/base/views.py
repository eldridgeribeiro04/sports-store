from django.shortcuts import render, redirect

from base.filter import ProductFilter, BrandFilter

from base.forms import BrandForm, CategoryForm, ProductForm, IncreaseProductForm
from base.models import Product, Category, Brand

from django.shortcuts import render, get_object_or_404

# Create your views here.

def home(request):
    products = Product.objects.all()
    brand = Brand.objects.all()
    
    myFilter = ProductFilter(request.GET, queryset=products)
    brand = myFilter.qs
    
    return render(request, 'base/home.html', {
        'brand': brand,
        'products': products,
        'myFilter': myFilter
        })
    
    
def most_viewed_products(request):
    most_viewed = Product.objects.order_by('-views')[:5]
    return render(request, 'base/home.html', {'most_viewed': most_viewed})
    

def filter_by_brand(request,brand_name):
    brand = get_object_or_404(Brand, brand_name=brand_name)
    products = Product.objects.filter(brand=brand)
    categories = Category.objects.all()
    category_id = request.GET.get('category')
    
    selected_category = None
    if category_id:
        selected_category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=selected_category, brand=brand)
    
    return render(request, 'base/brand_products.html', {
        'brand': brand,
        'products': products,
        'selected_category': selected_category,
        'categories': categories,
        })
    
    
def single_product_view(request, product_id, brand_name):
    brand = get_object_or_404(Brand, brand_name=brand_name)
    single_product = get_object_or_404(Product, brand=brand, pk=product_id)
    
    category = single_product.category
    
    related_products = Product.objects.filter(category=category).exclude(pk=product_id)[:3]
    other_products = Product.objects.all().exclude(pk=product_id)[:3]
    
    return render(request, 'base/single_product.html', {
        'single_product': single_product,
        'related_products': related_products,
        'other_products': other_products})
     


def add_brand(request):
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base:add_product')
    else:
        form = BrandForm()
    return render(request, 'base/add_brand.html', {'form': form})


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base:add_product')
        else:
            print(form.errors)
    else:
        form = CategoryForm()
    return render(request, 'base/add_category.html', {'form': form})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('base:home')
    else:
        form = ProductForm()
    return render(request, 'base/add_product.html', {'form': form})
        
    
def increase_quantity(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    if request.method == 'POST':
        form = IncreaseProductForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            if quantity == None:
                quantity = 1
                product.quantity += quantity
                product.save()
            else:
                product.quantity += quantity
                product.save()
            return redirect('base:product', product_id=product.id, brand_name=product.brand.brand_name)
    else:
        form = IncreaseProductForm(instance=product)
    return render(request, 'base/increase_quantity.html', {'form': form,
                                                           'product': product})