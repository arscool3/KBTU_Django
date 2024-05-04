from django.contrib import admin
from .models import Event, Participant, Organizer, Ticket, Sponsor, Profile

@admin.register(Event)
class Event(admin.ModelAdmin):
    pass

@admin.register(Participant)
class Event(admin.ModelAdmin):
    pass

@admin.register(Organizer)
class Event(admin.ModelAdmin):
    pass

@admin.register(Ticket)
class Event(admin.ModelAdmin):
    pass

@admin.register(Sponsor)
class Event(admin.ModelAdmin):
    pass

@admin.register(Profile)
class Event(admin.ModelAdmin):
    pass