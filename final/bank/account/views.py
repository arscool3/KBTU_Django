from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from .models import BankAccountType, UserAddress, UserBankAccount

from .forms import UserRegistrationForm, UserAddressForm
from .serializers import BankAccountTypeSerializer, UserAddressSerializer, UserBankAccountSerializer, UserSerializer

User = get_user_model()

class UserRegistrationView(APIView):
    form_class = UserRegistrationForm
    address_form_class = UserAddressForm
    serializer_class = UserSerializer
    template_name = 'account/user_registration.html'

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
            return Response(
                {'message': message, 'user': serializer.data},
                status=status.HTTP_201_CREATED
            )

        return render(request, self.template_name, {'registration_form': registration_form, 'address_form': address_form})

class UserLoginView(APIView):
    authentication_classes = []
    permission_classes = []
    form_class = AuthenticationForm
    template_name = 'account/user_login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  
        return render(request, self.template_name, {'form': form})

class LogoutView(APIView):
    pattern_name = 'home'

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            logout(self.request)
        return super().get_redirect_url(*args, **kwargs)
    

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
