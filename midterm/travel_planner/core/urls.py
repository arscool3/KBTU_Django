from django.urls import path
from .views import home, accommodation_search, ticket_search, add_ticket_to_cart, add_accommodation_to_cart, view_cart, view_session_data, TicketAPIView, AccommodationAPIView, PlaceAPIView, PlaceDetailView, TicketDetailView, AccommodationDetailView, delete_ticket_from_cart, delete_accommodation_from_cart, update_ticket_quantity, update_accommodation_quantity, payment_page, process_payment

urlpatterns = [
    path('', home, name='home'),
    path('accommodation-search/', accommodation_search, name='accommodation_search'),
    path('ticket-search/', ticket_search, name='ticket_search'),
    path('add_ticket_to_cart/<int:ticket_id>/', add_ticket_to_cart, name='add_ticket_to_cart'),
    path('add_accommodation_to_cart/<int:accommodation_id>/', add_accommodation_to_cart, name='add_accommodation_to_cart'),
    path('cart/', view_cart, name='cart'),
    path('view_session_data/', view_session_data, name='view_session_data'),
    path('payment/', payment_page, name='payment_page'),
    path('process_payment/', process_payment, name='process_payment'),


    path('places/', PlaceAPIView.as_view(), name='place-list-create'),
    path('places/<int:pk>/', PlaceDetailView.as_view(), name='place-retrieve-update-destroy'),
    path('tickets/', TicketAPIView.as_view(), name='ticket-list-create'),
    path('tickets/<int:pk>/', TicketDetailView.as_view(), name='ticket-retrieve-update-destroy'),
    path('accommodations/', AccommodationAPIView.as_view(), name='accommodation-list-create'),
    path('accommodations/<int:pk>/', AccommodationDetailView.as_view(), name='accommodation-retrieve-update-destroy'),
    path('delete-ticket/', delete_ticket_from_cart, name='delete_ticket_from_cart'),
    path('update-ticket/', update_ticket_quantity, name='update_ticket_quantity'),
    path('update-accommodation/', update_accommodation_quantity, name='update_accommodation_quantity'),
    path('delete-accommodation/', delete_accommodation_from_cart, name='delete_accommodation_from_cart'),
    
]
