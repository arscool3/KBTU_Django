from django.db import models


class FoodCategory(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="food_category_images/", blank=True, null=True)
