from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserRegistrationView, UserLoginView, LogoutView, BankAccountTypeViewSet, UserBankAccountViewSet, UserAddressViewSet

app_name = 'account'

router = DefaultRouter()
router.register(r'bank-account-types', BankAccountTypeViewSet, basename='bank-account-type')
router.register(r'user-bank-accounts', UserBankAccountViewSet, basename='user-bank-account')
router.register(r'user-addresses', UserAddressViewSet, basename='user-address')

urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name='user_registration'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', LogoutView.as_view(), name='user_logout'),
    path('', include(router.urls)),
]
