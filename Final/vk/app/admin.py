from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserInfo)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Group)
admin.site.register(Image)
admin.site.register(Subscription)