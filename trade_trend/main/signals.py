from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from .tasks import notify_user_of_order