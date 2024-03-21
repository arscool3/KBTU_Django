from django.contrib import admin
from .models import Corporation,Department,Employee,Project
admin.site.register(Corporation)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Project)