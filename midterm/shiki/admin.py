from django.contrib import admin
from .models import *


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = (
        'id',
        'title',
        'source',
        'score',
        'status',
    )
    list_editable = ('status',)
    list_filter = ('status', 'genre')


@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = (
        'id',
        'title',
        'volumes',
        'score',
        'status',
    )
    list_editable = ('status',)
    list_filter = ('status', 'genre')


@admin.register(LightNovel)
class LightNovelAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = (
        'id',
        'title',
        'volumes',
        'score',
        'status',
    )
    list_editable = ('status',)
    list_filter = ('status', 'genre')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    class AnimeInline(admin.TabularInline):
        model = Anime
        extra = 1
    ordering = ('id',)
    list_display = (
        'id',
        'name',
        'description'
    )
    inlines = (AnimeInline,)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = (
        'id',
        'anime',
        'manga',
        'light_novel',
        'image'
    )

