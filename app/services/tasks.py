import dramatiq
from dramatiq.brokers.redis import RedisBroker

redis_broker = RedisBroker(host="localhost", port=6379)
dramatiq.set_broker(redis_broker)

@dramatiq.actor
def process_video(video_id: int):
    # Video processing logic here
    pass
