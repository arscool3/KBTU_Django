import uuid

from django.db import models

from food_categories.models import FoodCategory


class Food(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="food_images/", blank=True, null=True)
    price = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    category = models.ForeignKey(to=FoodCategory, on_delete=models.CASCADE, related_name="foods")

    def __str__(self):
        return f"{self.name}"
