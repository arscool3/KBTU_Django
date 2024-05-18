from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('auth/signin/',signin,name='signin'),
    path('auth/signup/',signup,name='signup'),
    path('auth/signup_mfr/',signup,name='signup_mfr'),
    path('auth/signout/',signout,name='signout'),
    path('profile/',profile,name='profile'),
    path('categories/',categories,name='categories'),
    path('categories/<int:id>',categories,name='category')
]