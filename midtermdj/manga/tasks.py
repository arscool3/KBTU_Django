from celery import shared_task
from .models import Manga

@shared_task
def update_manga_ratings():
    for manga in Manga.objects.all():
        reviews = manga.reviews.all()
        if reviews.exists():
            avg_rating = sum(review.rating for review in reviews) / reviews.count()
            manga.average_rating = avg_rating
            manga.save()

