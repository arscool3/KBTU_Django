# In your app directory, create a new file named forms.py

from django import forms
from .models import Product, Category, Cart, Order, Customer

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'image', 'quantity']

    image = forms.ImageField()  # Include the image field in the form

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['username', 'email', 'password', 'shipping_address', 'billing_address']

class OrderForm(forms.ModelForm):
    class Meta: 
        model =Order
        fields = ['order_date', 'customer', 'product', 'price', 'amount' ]