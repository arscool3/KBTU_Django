from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.apps import apps

app = apps.get_app_config('core')

for model_name, model in app.models.items():
    admin.site.register(model)

#admin.site.register(User, UserAdmin)