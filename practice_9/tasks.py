import dramatiq
from dramatiq.results.errors import ResultMissing
from cosmetic_services import anti_aging_service, skin_care_service, hair_care_service
from dramatiq.results.backends.redis import RedisBackend
from dramatiq.brokers.redis import RedisBroker
from dramatiq.results import Results

result_backend = RedisBackend()
redis_broker = RedisBroker()
redis_broker.add_middleware(Results(backend=result_backend))
dramatiq.set_broker(redis_broker)

@dramatiq.actor(store_results=True)
def add_cosmetic_task(id: str):
    print('started')
    result = anti_aging_service(id) & skin_care_service(id) & hair_care_service(id)
    print('ended', result)
    return result
