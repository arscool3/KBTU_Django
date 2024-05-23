import dramatiq
from dramatiq.brokers.redis import RedisBroker

broker = RedisBroker(url="redis://127.0.0.1:6379/0")
dramatiq.set_broker(broker)