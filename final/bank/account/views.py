from django.conf import settings
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.http import JsonResponse


from .models import BankAccountType, UserAddress, UserBankAccount

from .forms import UserRegistrationForm, UserAddressForm
from .serializers import BankAccountTypeSerializer, UserAddressSerializer, UserBankAccountSerializer, UserSerializer

User = get_user_model()

from django.shortcuts import redirect

class UserRegistrationView(APIView):
    form_class = UserRegistrationForm
    address_form_class = UserAddressForm
    serializer_class = UserSerializer
    template_name = 'account/user_registration.html'
    login_url = '/account/login/'
    home_url = '/'

    def get(self, request, *args, **kwargs):
        registration_form = self.form_class()
        address_form = self.address_form_class()
        return render(request, self.template_name, {'registration_form': registration_form, 'address_form': address_form})

    def post(self, request, *args, **kwargs):
        registration_form = self.form_class(request.POST)
        address_form = self.address_form_class(request.POST)

        if registration_form.is_valid() and address_form.is_valid():
            user = registration_form.save()
            address = address_form.save(commit=False)
            address.user = user
            address.save()

            login(request, user)
            serializer = self.serializer_class(user)
            message = (
                f'Thank You For Creating A Bank Account. '
                f'Your Account Number is {user.account.account_no}.'
            )
            return redirect(self.home_url)


        return render(request, self.template_name, {'registration_form': registration_form, 'address_form': address_form})

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

class UserLoginView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        return render(request, 'account/user_login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home') 
        else:
            errors = {}
            for field, field_errors in form.errors.items():
                errors[field] = field_errors[0]  # Take only the first error for each field
            return render(request, 'account/user_login.html', {'form': form, 'incorrect_input': True})


class LogoutView(APIView):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
        return redirect('home')  
    

class BankAccountTypeViewSet(viewsets.ModelViewSet):
    queryset = BankAccountType.objects.all()
    serializer_class = BankAccountTypeSerializer
    permission_classes = [IsAuthenticated]

class UserBankAccountViewSet(viewsets.ModelViewSet):
    queryset = UserBankAccount.objects.all()
    serializer_class = UserBankAccountSerializer
    permission_classes = [IsAuthenticated]

class UserAddressViewSet(viewsets.ModelViewSet):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer
    permission_classes = [IsAuthenticated]
