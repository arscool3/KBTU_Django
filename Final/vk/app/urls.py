from django.urls import path
from .views import *

urlpatterns = [
    path('posts/', postspage, name='home'),
    path('posts/<int:p_id>', postpage, name='postpage'),

    path('people/', people, name='people'),
    path('people/<int:p_id>', person, name='person'),
    path('people/me/', mypage, name='mypage'),

    path('groups/', groups, name='groups'),
    path('groups/<int:g_id>', group, name='group'),

    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('reg/', RegisterUser.as_view(), name='reg'),
]