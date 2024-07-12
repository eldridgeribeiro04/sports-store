from typing import Any
from django import forms

from base.models import Brand, Category, Product


class BrandForm(forms.ModelForm):
    brand_name = forms.CharField(
        max_length=100,
        label='Brand Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Brand Name'}
    ))
    
    class Meta:
        model = Brand
        fields = ['brand_name']
        
    def clean_name(self):
        name = self.cleaned_data.get('brand_name')
        if Brand.objects.filter(brand_name=name).exists():
            raise forms.ValidationError('Brand name already exists.')
        return name
    
    
class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = ['category_name']
        
    def clean_name(self):
        name = self.cleaned_data.get('category_name')
        if Category.objects.filter(category_name=name).exists():
            raise forms.ValidationError('Category name already exists.')
        return name
    
    
class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = '__all__'
        
    
class IncreaseProductForm(forms.ModelForm):
    
    # amount = forms.IntegerField(label='Amount', help_text='Enter a positive number')
    
    class Meta:
        model = Product
        fields = ['quantity',]
        
    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity <= 0:
            raise forms.ValidationError('Quantity must be a positive number.')
        return quantity
        
    # def __init__(self, *args, **kwargs):
    #     super(IncreaseProductForm, self).__init__(*args, **kwargs)
    #     self.fields['quantity'].widget.attrs['readonly'] = True
