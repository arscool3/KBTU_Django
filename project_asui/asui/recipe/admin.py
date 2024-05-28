from django.contrib import admin
from recipe.models import Recipe, Direction, MeasurementUnit, MeasurementQuantity, RecipeIngredient, Review, Ingredient


# Register your models here.
@admin.register(Recipe)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author')


admin.site.register(Direction)
admin.site.register(MeasurementUnit)
admin.site.register(MeasurementQuantity)
admin.site.register(RecipeIngredient)
admin.site.register(Review)
admin.site.register(Ingredient)