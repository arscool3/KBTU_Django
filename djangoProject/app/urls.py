from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.posts_list, name='posts_list'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('posts/<int:post_pk>/comments/', views.comments_list, name='comments_list'),
    path('posts/<int:post_pk>/comments/<int:pk>/', views.comment_detail, name='comment_detail'),
    # Assuming you're using POST method from forms for these:
    path('posts/create/', views.create_post, name='create_post'),
    path('comments/create/', views.create_comment, name='create_comment'),
]
