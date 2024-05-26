from django.urls import path
from .views import put_endpoint, post_endpoint, delete_endpoint, get_endpoint

urlpatterns = [
    path('put/', put_endpoint, name='put_endpoint'),
    path('post/', post_endpoint, name='post_endpoint'),
    path('delete/<int:test_id>/', delete_endpoint, name='delete_endpoint'),
    path('get/<int:test_id>/', get_endpoint, name='get_endpoint'),
]