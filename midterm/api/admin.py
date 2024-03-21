from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Message)
admin.site.register(ChatRoom)
admin.site.register(Notification)
admin.site.register(Attachment)
admin.site.register(OnlineUser)