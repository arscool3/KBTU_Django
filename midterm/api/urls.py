from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('test/', test),

    path('chat_app/', chat_page, name='chat-page'), #GET
    path('auth/sign_in/', LoginView.as_view(template_name="Login.html"), name="login-user"), #POST
    path('auth/sign_out/<str:username>/', LogoutViewCustom.as_view(), name="logout-user"), #GET
    path('auth/register/', register, name='register-user'), #post
    path('save_messages/', save_message, name='save_messages'), #POST
    path('get_messages/', get_message, name='get_messages'), #GET
    path('create_room/', create_room, name='create_room'), #POST
    path('get_rooms/', get_groups, name='get_groups'), #GET
    path('get_the_room/<str:room_name>/', get_the_group, name='get-room'),#GET
    path('save_message/<str:room_name>/', save_message_by_room, name='save-message-room'), #POST
    path('get_users/', get_online_users, name="online-users"), #GET
    path('set_user_activity/<str:username>/', set_users_activity, name="set-activity-user"), #POST
    path('set_notification/<str:username>/', set_notification, name="set-notification") #POST


]
