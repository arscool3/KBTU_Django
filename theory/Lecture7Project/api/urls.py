from django.urls import path
from .views import *
urlpatterns = [
    path('create/users/', createUser),
    path('create/commentary/', create_commentary),
    path('crate/official_answer/', create_official_answer),
    path('create/delete/commentary/', delete_commentary),
    path('get/users/', getUsers),
    path('get/comments/', get_all_commentaries),
    path('get/commentaries/<int:commentary_id>/', get_commentary_by_id),
    path('get/comments-by-user/<int:user_id>/', get_comments_by_user),
]