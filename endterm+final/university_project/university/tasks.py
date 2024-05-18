import dramatiq
from dramatiq.brokers.redis import RedisBroker
from dramatiq.results import Results
from dramatiq.results.backends.redis import RedisBackend

from .models import Course

REDIS_URL = "redis://localhost:6379/0"

result_backend = RedisBackend(url=REDIS_URL)
redis_broker = RedisBroker(url=REDIS_URL)
redis_broker.add_middleware(Results(backend=result_backend))
dramatiq.set_broker(redis_broker)


@dramatiq.actor
def update_course_description(course_id, new_description):
    try:
        course = Course.objects.get(pk=course_id)
        course.description = new_description
        course.save()
        return f"Description for Course '{course.name}' updated successfully."
    except Course.DoesNotExist:
        return f"Course with id '{course_id}' does not exist."
    except Exception as e:
        return f"An error occurred: {str(e)}"
