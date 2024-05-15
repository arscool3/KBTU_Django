import dramatiq
from dramatiq.brokers.redis import RedisBroker
from passlib.context import CryptContext
from redis import Redis


# redis_broker = RedisBroker(host="localhost", port=6379)
# dramatiq.set_broker(redis_broker)

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
redis_client = Redis(host="localhost", port=6379, db=0)


@dramatiq.actor
def hash_password_and_save(username: str, password: str):
    hashed_password = bcrypt_context.hash(password)
    redis_client.set(username, hashed_password)

