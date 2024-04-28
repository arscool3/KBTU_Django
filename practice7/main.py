import dramatiq
from dramatiq.brokers.redis import RedisBroker
from dramatiq.results import Results
from dramatiq.results.backends.redis import RedisBackend
from gov import crime_service, psycho_service, drugs_service

result_backend = RedisBackend()
redis_broker = RedisBroker()
redis_broker.add_middleware(Results(backend=result_backend))
dramatiq.set_broker(redis_broker)


@dramatiq.actor(store_results=True)
def ask_papers_score(paper_id):
    import time
    time.sleep(5) # exammple delay for getting data
    academic_scores = {"paper_id": paper_id, "score": 4.9}
    return academic_scores