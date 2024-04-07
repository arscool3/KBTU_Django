import dramatiq
from dramatiq.brokers.redis import RedisBroker
from dramatiq.results import Results
from dramatiq.results.backends.redis import RedisBackend

from email_service import send_email


result_backend = RedisBackend()
redis_broker = RedisBroker()
redis_broker.add_middleware(Results(backend=result_backend))
dramatiq.set_broker(redis_broker)

@dramatiq.actor(store_results=True)
def send_email_task(to: str, subject: str, body: str):

    return send_email(to, subject, body)


