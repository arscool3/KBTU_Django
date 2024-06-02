from django.urls import path
from core.views import *

urlpatterns = [
    path('', index, name='index'),
    path('auth/signin/',signin,name='signin'),
    path('auth/signup/',signup,name='signup'),
    path('auth/signup_mfr/',signup_mfr,name='signup_mfr'),
    path('auth/signout/',signout,name='signout'),
    path('profile/',profile,name='profile'),
    path('catalogue/<int:id>',category,name='category'),
    path('items/<int:id>',product,name='product'),
    path('items/buy/<int:id>',buy_product,name='buy_product'),
    path('items/new',new_product,name='new_product')
]