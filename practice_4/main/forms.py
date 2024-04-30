from django import forms
from .models import Product, Order, Customer

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'quantity']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name']

