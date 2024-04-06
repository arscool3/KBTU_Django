from django import forms
from.models import Author, Book, Category, Consumer, Review
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
  class Meta:
    model = Category
    fields = '__all__'

class BookForm(forms.ModelForm):
  class Meta:
    model = Book
    fields = '__all__'

class ReviewForm(forms.ModelForm):
  class Meta:
    model = Review
    fields = '__all__'
    
class AuthorForm(forms.ModelForm):
  class Meta:
    model = Author
    fields = '__all__'

class ConsumerForm(forms.ModelForm):
  class Meta:
    model = Consumer
    fields = '__all__'