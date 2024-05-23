from django.contrib import admin
from .models import Place, Accommodation, Ticket, Tour

# Регистрируем модели для админ-панели
admin.site.register(Place)
admin.site.register(Accommodation)
admin.site.register(Ticket)
admin.site.register(Tour)
