from django.contrib import admin
from .models.category import Category
from .models.book import Book
from .models.review import Review
from .models.rating import Rating
from .models.userlist import UserList
from django.contrib.admin import SimpleListFilter
# admin.site.register(Category)



# Register your models here.
class ABCFilter(SimpleListFilter):
    title = 'alphabetically filter'
    parameter_name = 'alphabetically filter'
    def lookups(self,request,model_admin):
        return(
            ('sorted by title',('sorted by title')),
            ('sorted by title reversed',('sorted by title reversed')),
            ('sorted by author',('sorted by author')),
            ('sorted by author reversed',('sorted by author reversed')),
            ('sorted by category',('sorted by category')),
            ('sorted by category reversed',('sorted by category reversed')),
            ('sorted by pages',('sorted by pages')),
            ('sorted by pages reversed',('sorted by pages reversed'))
        )
    def queryset(self,request,queryset):
        if not self.value():
            return queryset
        if self.value() == 'sorted by title':
            return queryset.order_by('title')
        if self.value() == 'sorted by title reversed':
            return queryset.order_by('-title')
        if self.value() == 'sorted by author':
            return queryset.order_by('author')
        if self.value() == 'sorted by author reversed':
            return queryset.order_by('-author')
        if self.value() == 'sorted by category':
            return queryset.order_by('category__name')
        if self.value() == 'sorted by category reversed':
            return queryset.order_by('-category__name')
        if self.value() == 'sorted by pages':
            return queryset.order_by('pages')
        if self.value() == 'sorted by pages reversed':
            return queryset.order_by('-pages')
class ABCFilterCategory(SimpleListFilter):
    title = 'alphabetically filter'
    parameter_name = 'alphabetically filter'
    def lookups(self,request,model_admin):
        return(
            ('sorted by name',('sorted by name')),
            ('sorted by name reversed',('sorted by name reversed'))
        )
    def queryset(self,request,queryset):
        if not self.value():
            return queryset
        if self.value() == 'sorted by name':
            return queryset.order_by('name')
        if self.value() == 'sorted by name reversed':
            return queryset.order_by('-name')
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_filter = (ABCFilterCategory,)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title','author','category','pages')
    list_filter = (ABCFilter,)
@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id','book')
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id','review')

@admin.register(UserList)
class UserListAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'user')