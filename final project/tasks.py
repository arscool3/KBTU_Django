import dramatiq

from dramatiq.brokers.redis import RedisBroker
from dramatiq.results import Results
from dramatiq.results.backends.redis import RedisBackend

from flora import ingredients_area_service, ingredients_rising_period_service

result_backend = RedisBackend()
redis_broker = RedisBroker()
redis_broker.add_middleware(Results(backend=result_backend))
dramatiq.set_broker(redis_broker)


@dramatiq.actor(store_results=True)
def add_employee_task(ingredient_id: str):
    print('started')
    result = ingredients_area_service(ingredient_id) & ingredients_rising_period_service(ingredient_id)
    print('ended', result)
    return result