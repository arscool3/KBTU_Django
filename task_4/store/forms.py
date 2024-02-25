from django import forms
from .models import Category, Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'description']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'}))