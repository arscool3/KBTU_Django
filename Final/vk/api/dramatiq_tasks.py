import dramatiq
from app.models import UserInfo

from dramatiq.brokers.redis import RedisBroker

redis_broker = RedisBroker()
dramatiq.set_broker(redis_broker)

@dramatiq.actor()
def createUserInfo(user):
   print("Ok")
   UserInfo.objects.create(user=user)


# docker run --name redis -p 6379:6379 redis/redis-stack-server:latest
