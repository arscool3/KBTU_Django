from django import forms
from core.models import *

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

class CustomerForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)

class ManufacturerForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    descr = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)