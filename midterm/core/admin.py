from django.contrib import admin

from core.models import *

admin.site.register(Gist)

admin.site.register(Commit)

admin.site.register(File)
