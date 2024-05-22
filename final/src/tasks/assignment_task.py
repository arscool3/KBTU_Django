import dramatiq

from dramatiq.brokers.redis import RedisBroker
from dramatiq.results import Results
from dramatiq.results.backends.redis import RedisBackend
import time
import random
import redis

result_backend = RedisBackend()
redis_broker = RedisBroker()
redis_broker.add_middleware(Results(backend=result_backend))
dramatiq.set_broker(redis_broker)

redis_client = redis.Redis(host='localhost', port=6379, db=0)


@dramatiq.actor(store_results=True)
def load_assignment_task(assignment_id: int):
    total_progress = 100
    progress = 0
    while progress < total_progress:
        time.sleep(random.uniform(0.1, 0.5))
        progress += random.randint(1, 10)
        print(progress)
        redis_client.set(assignment_id, progress)
    result = "Assignment loaded successfully"
    redis_client.set(assignment_id, result)

