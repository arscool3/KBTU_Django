from django import forms
from .models import MyModel
from .models import Product, Order


class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['field1', 'field2']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['products', 'total_price']

