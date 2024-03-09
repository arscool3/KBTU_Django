from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('test/', test),

    path('chatApp/', chatPage, name='chat-page'), #GET
    path('auth/sign_in/', LoginView.as_view(template_name="Login.html"), name="login-user"), #POST
    path('auth/sign_out/<str:username>/', LogoutViewCustom.as_view(), name="logout-user"),

    path('save-messages/', save_message, name='save_messages'), #POST
    path('get-messages/', get_message, name='get_messages'), #GET
    path('create-room/', create_room, name='create_room'), #POST
    path('get-rooms/', get_groups, name='get_groups'), #GET
    path('get-the-room/<str:room_name>/', get_the_group, name='get-room'),#GET
    path('save-message/<str:room_name>/', save_message_by_room, name='save-message-room'), #POST
    path('get-users/', get_online_users, name="online-users"), #GET
    path('set-user-activity/<str:username>/', set_users_activity, name="set-activity-user"), #POST


]
