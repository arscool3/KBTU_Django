from django.db import models
from django.db.models import Avg


# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')
    reviews = models.IntegerField()
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    difficulty = models.CharField(max_length=255)
    prep_time = models.IntegerField()
    cook_time = models.IntegerField()
    servings = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='recipes', default='assets/spaghetti.jpeg')

    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'

    @property
    def num_of_reviews(self):
        return self.review_set.count()

    @property
    def average_rating(self) -> float:
        return Review.objects.filter(recipe=self).aggregate(Avg("rating"))["rating__avg"] or 0

    def __str__(self):
        return f'{self.id}: {self.title}, email: {self.author}'


class Direction(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='directions', on_delete=models.CASCADE)
    step = models.IntegerField()
    content = models.TextField(default='')

    class Meta:
        verbose_name = 'Direction'
        verbose_name_plural = 'Directions'

    def __str__(self):
        return f'{self.recipe.title}: {self.step}'


class MeasurementUnit(models.Model):
    unit = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'MeasurementUnit'
        verbose_name_plural = 'MeasurementUnits'

    def __str__(self):
        return self.unit


class MeasurementQuantity(models.Model):
    qty = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'MeasurementQuantity'
        verbose_name_plural = 'MeasurementQuantities'

    def __str__(self):
        return self.qty


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    measurement_unit = models.ForeignKey(MeasurementUnit, on_delete=models.CASCADE)
    measurement_quantity = models.ForeignKey(MeasurementQuantity, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.recipe}: {self.measurement_quantity} {self.measurement_unit} of {self.ingredient}'


class Review(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.recipe.title + ": " + str(self.rating)
    

class Comment(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}: {self.text[:20]}...'
