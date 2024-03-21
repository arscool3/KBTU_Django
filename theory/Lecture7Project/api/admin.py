from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Userr)
class UserrAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email')

@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'official_answer', 'commentary_type_id')


@admin.register(OfficialAnswer)
class OfficialAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'created_at', 'user')

@admin.register(CommentaryType)
class CommentaryTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
