import dramatiq
from dramatiq.brokers.redis import RedisBroker
from data_processing import process_data, analyze_data

redis_broker = RedisBroker(host="localhost", port=6379)

dramatiq.set_broker(redis_broker)

@dramatiq.actor
def process_data_task(data):
    result = process_data(data)
    print(result)

@dramatiq.actor
def analyze_data_task(data):
    result = analyze_data(data)
    print(result)
