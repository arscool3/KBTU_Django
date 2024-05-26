from django.contrib import admin

from links_app.models import Category, Click, Link, LinkUsage, Tag, User

admin.site.register(User)

# Register the Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Register the Tag model
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Register the Link model
@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('url', 'title', 'category', 'created_by')
    search_fields = ('url', 'title')
    list_filter = ('category', 'tags')

# Register the Click model
@admin.register(Click)
class ClickAdmin(admin.ModelAdmin):
    list_display = ('link', 'timestamp')
    search_fields = ('link__url', 'link__title')

# Register the LinkUsage model
@admin.register(LinkUsage)
class LinkUsageAdmin(admin.ModelAdmin):
    list_display = ('link', 'clicks')
    search_fields = ('link__url', 'link__title')
# Register your models here.
