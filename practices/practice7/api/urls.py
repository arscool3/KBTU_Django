from django.urls import path
from .views import create_subscriber, create_post, blogpost_list, blogpost_detail



urlpatterns = [
    path('post/', create_post, name='create-post'),
    path('subscriber', create_subscriber, name='create-subscriber'),
    path('posts/', blogpost_list, name='blogpost-list'),
    path('post/<int:pk>', blogpost_detail, name='blogpost-detail'),

]
