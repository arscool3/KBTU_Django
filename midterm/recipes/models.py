from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

class Recipe(models.Model):
  title = models.CharField(max_length=100)
  category = models.ManyToManyField(Category, related_name='recipes')
  author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  description = models.TextField()
  time_required = models.IntegerField(default = 10)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title  
  
  @property
  def instructions(self):
    return self.instructions.all()

  @property
  def ingredients(self):
    return self.ingredients.all()

class Ingredient(models.Model):
  name = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

  
class Instruction(models.Model):
  step = models.IntegerField()
  description = models.TextField()
  recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='instructions')
  ingredients = models.ManyToManyField(Ingredient, related_name='instructions')
  time_required = models.IntegerField(default = 1)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f'{self.recipe.title} - Step {self.step}'
  
class Comment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
  comment = models.TextField()
  rating = models.IntegerField(default=1)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f'{self.user.username} - {self.recipe.title}'
  