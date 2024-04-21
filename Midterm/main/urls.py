from django.urls import path

from .views import get_flights, search_ticket, login_view, logout_view, register_view, entry_page, admin_view, aircraft_time_scheduling, AircraftByFlightIdView

urlpatterns = [
    path("get_flights/", get_flights, name="get_flights"),
    path("search_ticket/", search_ticket, name="search_ticket"),
    path("", entry_page, name="entry_page"),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path("logout/", logout_view, name='logout'),
    path("admin_page/", admin_view, name='admin_page'),
    path("aircraft_time_scheduling/", aircraft_time_scheduling, name='aircraft_time_scheduling'),
    path("api/aircraft_by_flight_id/", AircraftByFlightIdView.as_view(), name='aircraft_by_flight_id'),
]