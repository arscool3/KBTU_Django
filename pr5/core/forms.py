from django import forms

from models import *


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'


class BorrowForm(forms.ModelForm):
    class Meta:
        model = BorrowedBook
        fields = '__all__'
