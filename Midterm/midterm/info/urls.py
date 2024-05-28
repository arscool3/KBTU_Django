from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.get_events, name='get_events'), #GET
    path('events/<int:event_id>/', views.get_event, name='get_event'), #GET
    path('events/<int:event_id>/participants/', views.get_event_participants, name='get_event_participants'),   #GET
    path('users/<int:user_id>/tickets/', views.get_user_tickets, name='get_user_tickets'),   #GET
    path('users/<int:user_id>/profile/', views.get_user_profile, name='get_user_profile'),  #GET
    path('events/<int:event_id>/sponsors/', views.get_event_sponsors, name='get_event_sponsors'), #GET
    path('events/create/', views.create_event, name='create_event'),  #POST
    path('events/<int:event_id>/register/', views.register_participant, name='register_participant'), #POST
    path('organizers/create/', views.create_organizer, name='create_organizer'), #POST
    path('events/<int:event_id>/purchase/', views.purchase_ticket, name='purchase_ticket'), #GET
    path('events/<int:event_id>/sponsor/add/', views.add_sponsor, name='add_sponsor'),  #POST
    path('users/<int:user_id>/profile/update/', views.update_profile, name='update_profile'), #POST
]
