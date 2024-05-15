import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zhumystap.settings')
django.setup()
import dramatiq
from dramatiq.results.backends.redis import RedisBackend
from dramatiq.brokers.redis import RedisBroker
from dramatiq.results import Results, ResultMissing
from .models import User, Notification


result_backend = RedisBackend()
broker = RedisBroker()
broker.add_middleware(Results(backend=result_backend))
dramatiq.set_broker(broker)


@dramatiq.actor
def activate_vacancy_notification(vacancy):
    users = User.objects.all()
    print(users)
    for user in users:
        Notification.objects.create(
            user=user,
            message=f"Vacancy activated. {vacancy.get('title')} : {vacancy.get('description')}",
        )
