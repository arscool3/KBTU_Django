import dramatiq
from services import check_criminal_record, evaluate_skills, conduct_interview


from dramatiq.brokers.redis import RedisBroker
from dramatiq.results import Results
from dramatiq.results.backends.redis import RedisBackend

broker = RedisBroker(url="redis://localhost:6379/0")
result_backend = RedisBackend(url="redis://localhost:6379/1")
broker.add_middleware(Results(backend=result_backend))
dramatiq.set_broker(broker)

@dramatiq.actor(store_results=True)
def check_candidate_task(candidate_id: int):
    print(f"Checking candidate {candidate_id}")
    record_result = check_criminal_record(candidate_id)
    skills_result = evaluate_skills(candidate_id)
    interview_result = conduct_interview(candidate_id)
    return {
        "record_check": record_result,
        "skills_evaluation": skills_result,
        "interview": interview_result
    }
