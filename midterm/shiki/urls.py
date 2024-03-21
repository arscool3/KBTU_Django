from django.urls import path
from .views import *

app_name = "shiki"

urlpatterns = [
    path('anime/create/', anime_create, name='anime_create'),
    path('manga/create/', manga_create, name='manga_create'),
    path('light_novel/create/', light_novel_create, name='light_novel_create'),
    path('genres/create/', genre_create, name='genre_create'),
    path('genres/', genre_list, name='genre_list'),
    path('genres/<int:genre_id>/', genre_read, name='genre_read'),
    path('genres/<int:genre_id>/update/', genre_update, name='genre_update'),
    path('genres/<int:genre_id>/delete/', genre_delete, name='genre_delete'),
    path('signup/', signup, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logged_out'),
    path('anime/', anime_list, name='anime_list'),
    path('anime/<int:anime_id>/', anime_read, name='anime_read'),
    path('anime/<int:anime_id>/update/', anime_update, name='anime_update'),
    path('anime/<int:anime_id>/delete/', anime_delete, name='anime_delete'),
    path('profile/', profile, name='profile'),

]
