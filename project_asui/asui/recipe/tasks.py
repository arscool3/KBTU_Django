import os
import django
import dramatiq
from dramatiq.brokers.redis import RedisBroker
from django.db.models import Avg


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "asui.settings")
django.setup()
from recipe.models import Review, Recipe, Comment
from . import models

redis_broker = RedisBroker(url="redis://localhost:6379/0")
dramatiq.set_broker(redis_broker)


@dramatiq.actor
def process_review(review_id):
    review = Review.objects.get(pk=review_id)
    if review.comment:
        Comment.objects.create(user=review.user, recipe=review.recipe, text=review.comment)
        print(f"Комментарий добавлен: {review.comment}")

    recipe = review.recipe
    new_average_rating = Review.objects.filter(recipe=recipe).aggregate(models.Avg('rating'))['rating__avg'] or 0
    recipe.average_rating = new_average_rating
    recipe.save()
    print(f"Средний рейтинг для '{recipe.title}' пересчитан: {new_average_rating}")
