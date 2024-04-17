import dramatiq


from dramatiq.brokers.redis import RedisBroker
from dramatiq.results import Results
from dramatiq.results.backends.redis import RedisBackend

from main import get_city_timezone


result_backend = RedisBackend()
redis_broker = RedisBroker()
redis_broker.add_middleware(Results(backend=result_backend))
dramatiq.set_broker(redis_broker)


@dramatiq.actor(store_results=True)
def get_timezone(city: str):
    print("Started")
    result = get_city_timezone(city)
    print("Ended", result)
    return result
