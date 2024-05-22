from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User
from .tasks import user_update_task


@receiver(post_save, sender=User)
def user_updated(sender, instance, **kwargs):
    if instance.pk:
        user_update_task.send(instance.email)
