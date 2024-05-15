from django.contrib import admin

from core.models import Event, Organizer, Student

admin.site.register(Event)
admin.site.register(Organizer)
admin.site.register(Student)