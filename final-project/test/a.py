import dramatiq
from pprint import pprint
from dramatiq.brokers.redis import RedisBroker

redis_broker = RedisBroker(host="localhost", port=6379)
dramatiq.set_broker(redis_broker)


@dramatiq.actor
def poll_odds_sport_radar():
    pprint("poller for sport radar should be implemented here")


if __name__ == "__main__":
    poll_odds_sport_radar.send()
