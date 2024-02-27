from django import forms
from test_app.models import Customer

class NewCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"