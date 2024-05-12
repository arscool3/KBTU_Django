from django.db import models

from foods.models import Food
from orders.choices import StatusChoices
from users.models import User


class Order(models.Model):
    customer = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="orders")
    food = models.ForeignKey(to=Food, on_delete=models.CASCADE, related_name="order")
    special_wishes = models.TextField(blank=True, default="")
    amount = models.FloatField(default=1)
    status = models.CharField(choices=StatusChoices.choices, default=StatusChoices.Waiting)
    order_identifier = models.IntegerField(default=0)
