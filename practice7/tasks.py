import dramatiq

from dramatiq.brokers.redis import RedisBroker
from dramatiq.results import Results

from dramatiq.results.backends.redis import RedisBackend
from tests import test_checker

result_back = RedisBackend()
redis_broker = RedisBroker()

redis_broker.add_middleware(Results(backend=result_back))

dramatiq.set_broker(redis_broker)

@dramatiq.actor(store_results = True)
def testing_task(id: int):
    print("Starting")
    result = test_checker(id)
    print("End", result)
    return result