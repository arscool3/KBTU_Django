from django.urls import path, include, re_path
from .clients import *

# Here, "" is routing to the URL ChatConsumer which
# will handle the chat functionality.
websocket_urlpatterns = [
    path("", ChatConsumer.as_asgi()),
    re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatRoomConsumer.as_asgi()),
]