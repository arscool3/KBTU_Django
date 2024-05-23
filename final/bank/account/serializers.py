from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import BankAccountType, UserAddress, UserBankAccount

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']

class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ['street_address', 'city', 'postal_code', 'country']

class UserBankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBankAccount
        fields = ['account_no', 'gender', 'birth_date', 'account_type', 'user']



class BankAccountTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccountType
        fields = '__all__'
