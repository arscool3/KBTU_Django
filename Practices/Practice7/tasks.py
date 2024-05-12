# tasks.py
import dramatiq

from dramatiq.brokers.redis import RedisBroker
from dramatiq.results import Results
from dramatiq.results.backends.redis import RedisBackend

from stock import *

result_backend = RedisBackend()
redis_broker = RedisBroker()
redis_broker.add_middleware(Results(backend=result_backend))
dramatiq.set_broker(redis_broker)


@dramatiq.actor(store_results=True)
def CheckStock_task(artiqul: str):
    print('started')
    result = check([stock1_service(artiqul), stock2_service(artiqul),stock2_service(artiqul)])
    print('ended', result)
    return result
