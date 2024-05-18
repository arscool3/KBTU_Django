import os

import django
import dramatiq
from dramatiq.brokers.redis import RedisBroker
from dramatiq.results import Results
from dramatiq.results.backends.redis import RedisBackend
from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Category

result_backend = RedisBackend()
redis_broker = RedisBroker()
redis_broker.add_middleware(Results(backend=result_backend))
dramatiq.set_broker(redis_broker)

# Установите DJANGO_SETTINGS_MODULE, если не установлен
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KBTU_Django.settings")
django.setup()


@receiver(pre_save, sender=Category)
def category_updated(sender, instance, **kwargs):
    if instance.pk:
        category_update_task.send(instance.id)


@dramatiq.actor(store_results=True)
def category_update_task(category_id):
    category = Category.objects.get(id=category_id)
    category.name += "!"
    category.save()
    return f"Category {category_id} updated successfully."
