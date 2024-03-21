from django.contrib import admin

from app.models import *

admin.site.register(Member)

admin.site.register(Trainer)

admin.site.register(Workout)

admin.site.register(MembershipPlan)

admin.site.register(Attendance)

admin.site.register(Payment)