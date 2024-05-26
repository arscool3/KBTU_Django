from django import forms

from Library.models import *


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = '__all__'

class PublishingOfficeForm(forms.ModelForm):
    class Meta:
        model = PublishingOffice
        fields = '__all__'

