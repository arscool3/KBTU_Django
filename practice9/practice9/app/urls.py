from django.urls import path
from . import views

urlpatterns = [
    path('put/', views.put_endpoint, name='put'),
    path('post/', views.post_endpoint, name='post'),
    path('delete/', views.delete_endpoint, name='delete'),
    path('get/', views.get_endpoint, name='get'),
]
