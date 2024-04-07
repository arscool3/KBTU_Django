import dramatiq

from dramatiq.brokers.redis import RedisBroker
from dramatiq.results import Results
from dramatiq.results.backends.redis import RedisBackend

from credit import check_credit_history, analyze_income, verify_identity

result_backend = RedisBackend()
redis_broker = RedisBroker()
redis_broker.add_middleware(Results(backend=result_backend))
dramatiq.set_broker(redis_broker)


@dramatiq.actor(store_results=True)
def evaluate_credit_task(ssn: str):
    print('Evaluation started for:', ssn)
    credit_history = check_credit_history(ssn)
    income_analysis = analyze_income(ssn)
    identity_verification = verify_identity(ssn)

    result = credit_history & income_analysis & identity_verification
    print('Evaluation ended for:', ssn, result)
    return result
