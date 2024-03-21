from django.contrib import admin
from .models import Instructor,Member,Workout,Equipment,Membership,Gym
# Register your models here.
admin.site.register(Instructor),
admin.site.register(Member),
admin.site.register(Membership),
admin.site.register(Workout),
admin.site.register(Gym)
admin.site.register(Equipment)