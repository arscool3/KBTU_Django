import dramatiq
from dramatiq.results.backends.redis import RedisBackend
from dramatiq.brokers.redis import RedisBroker
from dramatiq.results import Results
from background_task import process_payment_with_service

result_backend = RedisBackend()
broker = RedisBroker()
broker.add_middleware(Results(backend=result_backend))
dramatiq.set_broker(broker)


@dramatiq.actor(store_results=True)
def async_process_payment(payment_id, amount):

    print(f"Initiating payment processing for ID {payment_id} and amount ${amount}.")
    result = process_payment_with_service(payment_id, amount)

    if result and result.get("status") == "success":
        print(f"Payment processed successfully: {result}")
    else:
        print("Failed to process payment or payment declined.")