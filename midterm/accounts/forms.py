from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from accounts.models import Account

class AccountAuthenticationForm(AuthenticationForm):
    class Meta:
        model = Account
        fields = ['username', 'password']

class AccountCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Account
        fields = ['username', 'password1', 'password2']

