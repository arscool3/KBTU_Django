import dramatiq

from dramatiq.brokers.redis import RedisBroker
from dramatiq.results import Results
from dramatiq.results.backends.redis import RedisBackend
import time
import random

result_backend = RedisBackend()
redis_broker = RedisBroker()
redis_broker.add_middleware(Results(backend=result_backend))
dramatiq.set_broker(redis_broker)


@dramatiq.actor(store_results=True)
def load_assignment_task(assignment_id: int):
    total_progress = 100
    progress = 0
    while progress < total_progress:
        time.sleep(random.uniform(0.1, 0.5))
        progress += random.randint(1, 10)
        progress = min(progress, total_progress)
        load_assignment_task.send_progress(progress, total_progress)
    return f"Assignment {assignment_id} loaded successfully"