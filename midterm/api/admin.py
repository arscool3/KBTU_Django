from django.contrib import admin
from api.models import Organization, Role, User, Group, Room, Events


# Register your models here.

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'organization']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'role', 'organization', 'group']


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'organization']


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ['id', 'discipline', 'event_start_time', 'day', 'room', 'tutor', 'group']



