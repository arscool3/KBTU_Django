import os
import random
import sys
import logging

import dramatiq
from dramatiq.brokers.redis import RedisBroker
from dramatiq.results import Results
from dramatiq.results.backends.redis import RedisBackend


result_backend = RedisBackend()
redis_broker = RedisBroker(host=os.getenv("REDIS", "localhost"), port=os.getenv("REDIS_PORT", 6379))
redis_broker.add_middleware(Results(backend=result_backend))
dramatiq.set_broker(redis_broker)

logging.basicConfig(level=logging.INFO)


@dramatiq.actor
def add(x, y):
    result = x + y
    logging.info("The sum of %d and %d is %d.", x, y, result)
    return result

def main(count):
    for _ in range(count):
        add.send(random.randint(0, 1000), random.randint(0, 1000))


if __name__ == "__main__":
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    main(count)
