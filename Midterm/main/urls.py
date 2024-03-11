from django.urls import path

from .views import get_flights, search_ticket, login_view, check_view, logout_view, register_view, entry_page

urlpatterns = [
    path("get_flights/", get_flights, name="get_flights"),
    path("search_ticket/", search_ticket, name="search_ticket"),
    path("", entry_page, name="entry_page"),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('check/', check_view, name='check'),
    path("logout/", logout_view, name='logout')
]