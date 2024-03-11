from django.contrib import admin

from Project.models import *

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(Attachment)
admin.site.register(Team)