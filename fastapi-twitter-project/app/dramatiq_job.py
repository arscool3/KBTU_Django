import dramatiq
from dramatiq.results.backends.redis import RedisBackend
from dramatiq.brokers.redis import RedisBroker
from dramatiq.results import Results, ResultMissing

result_backend = RedisBackend()
broker = RedisBroker()
broker.add_middleware(Results(backend=result_backend))
dramatiq.set_broker(broker)

bad_citizens = [
    'Terrorist',
    'Killer',
    'Thief',
    'Festival',
    'Bandit'
]


@dramatiq.actor(store_results=True)
def check_valid_name(name: str)->str:
    for person_name in bad_citizens:
        if person_name == name:
            return "Dangerous"
    return 'ok'