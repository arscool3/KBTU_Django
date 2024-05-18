from django.contrib import admin
from .models import FitnessUser, Activity, Diet, HealthMetrics, Goal, CurrentProgress

admin.site.register(FitnessUser)
admin.site.register(Activity)
admin.site.register(Diet)
admin.site.register(HealthMetrics)
admin.site.register(Goal)
admin.site.register(CurrentProgress)


