from django import forms
from .models import Product, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'total_amount']


class OrderForm(forms.ModelForm):
    products = forms.ModelMultipleChoiceField(queryset=Product.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Order
        fields = ['customer_name', 'total_amount']
