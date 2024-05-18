import dataclasses
import time

import dramatiq

from dramatiq.brokers.redis import RedisBroker
from dramatiq.results import Results
from dramatiq.results.backends.redis import RedisBackend

result_backend = RedisBackend()
redis_broker = RedisBroker()
redis_broker.add_middleware(Results(backend=result_backend))
dramatiq.set_broker(redis_broker)


@dataclasses.dataclass
class Library:
    books_in_stock: list[int]


libraries = []  # other libraries that could have a book
result = []


@dramatiq.actor(store_results=True)
def check_book_task(book_id):
    for library in libraries:
        time.sleep(1)
        for book in library.books_in_stock:
            if book == book_id:
                result.append(library)
                continue

    return result
