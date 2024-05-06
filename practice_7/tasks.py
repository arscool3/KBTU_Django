import dramatiq

from dramatiq.brokers.redis import RedisBroker
from dramatiq.results import Results
from dramatiq.results.backends.redis import RedisBackend

from attestation1.practice_7.kitchen import sweets_department, gmo_dep, chemical_dep

result_backend = RedisBackend()
redis_broker = RedisBroker()
redis_broker.add_middleware(Results(backend=result_backend))
dramatiq.set_broker(redis_broker)


@dramatiq.actor(store_results=True)
def add_order_task(order_id: str):
    
    result = sweets_department(order_id) & gmo_dep(order_id) & chemical_dep(order_id)
    print('ended', result)
    return result