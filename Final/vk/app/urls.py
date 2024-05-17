from django.urls import path
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('posts/', postspage, name='home'),
    path('posts/<int:p_id>', postpage, name='postpage'),

    path('people/', people, name='people'),
    path('people/<int:p_id>', person, name='person'),
    path('people/me/', mypage, name='mypage'),
    path('ChangeUserInfo/', ChangeUserInfo, name='changeUserInfo'),

    path('groups/', groups, name='groups'),
    path('groups/<int:g_id>', group, name='group'),
    path('addGroup', addGroup, name='addGroup'),


    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('reg/', RegisterUser.as_view(), name='reg'),

    # Functions

    #Group

    path('subGroup/<int:g_id>', SubGroup, name='SubG'),
    path('unsubGroup/<int:g_id>', UnsubGroup, name='UnsubG'),

    #Post
    path('Like/<int:p_id>', like, name='like'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)