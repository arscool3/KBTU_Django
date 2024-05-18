from django import forms
from .models import *

class LoginForm(forms.ModelForm):
    class Meta:
    	model = User
    	fields = [
            'username', 
            'password',
    	]

class CategoryForm(forms.ModelForm):
    class Meta:
    	model = Category
        fields = "__all__"

class ProductForm(forms.ModelForm):
    class Meta:
    	model = Product
        fields = "__all__"

class HistoryItemForm(forms.ModelForm):
    class Meta:
    	model = HistoryItem
        fields = "__all__"

class CommentForm(forms.ModelForm):
    class Meta:
    	model = Comment
        fields = "__all__"

class CustomerForm(forms.ModelForm):
    class Meta:
    	model = Customer
        fields = [
            'username', 
            'password', 
            'email', 
            'first_name', 
            'last_name'
    	]

class ManufacturerForm(forms.ModelForm):
    class Meta:
    	model = Manufacturer
        fields = [
            'username', 
            'password', 
            'email', 
            'descr'
    	]