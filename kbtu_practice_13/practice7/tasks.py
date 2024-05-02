import dramatiq
from dramatiq.brokers.redis import RedisBroker
from dramatiq.results import Results
from dramatiq.results.backends.redis import RedisBackend
import random
import datetime

result_backend = RedisBackend()
redis_broker = RedisBroker()
redis_broker.add_middleware(Results(backend=result_backend))
dramatiq.set_broker(redis_broker)

def generate_random_weather(city: str) -> dict:
    temperature = random.randint(-10, 40)
    humidity = random.randint(10, 90)
    wind_speed = random.randint(0, 20)
    conditions = ["Clear", "Cloudy", "Rainy", "Snowy"]
    weather = {
        "city": city,
        "temperature": temperature,
        "humidity": humidity,
        "wind_speed": wind_speed,
        "condition": random.choice(conditions),
        "timestamp": datetime.datetime.now().isoformat(),
    }
    return weather

@dramatiq.actor(store_results=True)
def get_weather_task(city: str) -> dict:
    weather_data = generate_random_weather(city)
    return weather_data
