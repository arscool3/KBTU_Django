from django.urls import path

from .views import register_view, login_view, logout_view, application_page_view, manager_page_view, close_request_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('application_page/', application_page_view, name='application_page'),
    path('manager_page/', manager_page_view, name='manager_page'),
    path('close_request/<uuid:request_id>/', close_request_view, name='close_request'),
]