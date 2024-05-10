from django.urls import path
from .views import *

urlpatterns = [
    path('posts/', postspage, name='home'),
    path('posts/<int:p_id>', postpage),

    path('people', people, name='people'),
    path('groups', groups, name='groups'),
    path('me/', mypage, name='me'),

    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('reg/', RegisterUser.as_view(), name='reg'),
]