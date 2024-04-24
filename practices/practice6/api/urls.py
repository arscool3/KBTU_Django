
from django.urls import path
from .views import EventList, EventDetail, TicketList, TicketDetail, ScheduleDetail, ScheduleList



urlpatterns = [
    path('event/', EventList.as_view()),
    path('event/<int:event_id>', EventDetail.as_view()),
    path('ticket/', TicketList.as_view()),
    path('ticket/<int:ticket_id>', TicketDetail.as_view()),
    path('schedule/', ScheduleList.as_view()),
    path('schedule/<int:schedule_id>', ScheduleDetail.as_view()),
]
