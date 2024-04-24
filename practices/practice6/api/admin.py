from django.contrib import admin

from .models import Organizer, Event, Ticket, Attendee, Registration, Schedule



admin.site.register(Organizer)
admin.site.register(Event)
admin.site.register(Attendee)
admin.site.register(Ticket)
admin.site.register(Registration)
admin.site.register(Schedule)