import dramatiq
from dramatiq.brokers.redis import RedisBroker
from dramatiq.results import Results
from dramatiq.results.backends.redis import RedisBackend

from .models import Genre

result_backend = RedisBackend()
redis_broker = RedisBroker()
redis_broker.add_middleware(Results(backend=result_backend))
dramatiq.set_broker(redis_broker)


@dramatiq.actor(store_results=True)
def genre_update_task():
    genres = Genre.objects.all()

    for genre in genres:
        genre.description = "This is a placeholder description."
        genre.save()

    return "Genre update task completed successfully."
