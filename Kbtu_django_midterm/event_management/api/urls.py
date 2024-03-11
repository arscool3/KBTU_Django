from django.urls import path
from .views import event_list, event_detail, attendee_list, signup, signin, signout, event_schedule,ticket_detail,ticket_list, event_create, event_delete, schedule_create, ticket_create, create_attendee, event_by_organizer, tickets_by_event



urlpatterns = [
    # GET
    path('events/', event_list, name='event_list'),
    path('events/<int:event_id>/', event_detail, name='event_detail'),
    path('events/<int:event_id>/attendees/', attendee_list, name='attendee_list'),
    path('events/<int:event_id>/schedule/', event_schedule, name='event_schedule'),
    path('tickets/', ticket_list, name='ticket_list'),
    path('tickets/<int:ticket_id>/', ticket_detail, name='ticket_detail'),

    path('signout/', signout, name='signout'),

    # POST
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('events/create/', event_create, name='event_create'),
    path('events/<int:event_id>/delete/', event_delete, name='event_delete'),
    path('events/<int:event_id>/schedule/create/', schedule_create, name='schedule_create'),
    path('events/<int:event_id>/ticket/create/', ticket_create, name='ticket_create'),
    path('attendee/create', create_attendee, name='attendee_create'),

    # Testing custom managers
    path('events/<str:name>', event_by_organizer, name = 'event_by_organizer'),
    path('tickets/<int:event_id>/guests', tickets_by_event, name = 'tickets_by_event'),
]