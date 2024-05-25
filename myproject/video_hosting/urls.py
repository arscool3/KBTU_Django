from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.video_list, name='video_list'),
    path('video/<int:video_id>/', views.video_detail, name='video_detail'),
    path('video/upload/', views.upload_video, name='upload_video'),
    path('video/<int:video_id>/comment/', views.add_comment_to_video, name='add_comment_to_video'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

