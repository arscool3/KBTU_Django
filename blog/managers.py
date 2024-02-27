from django.db import models

class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published=True)
    def with_comments_count(self):
        return self.annotate(num_comments=models.Count('comment'))

    def by_author(self, author):
        return self.filter(author=author)

class CommentQuerySet(models.QuerySet):
    def approved(self):
        return self.filter(approved=True)
    def by_author(self, author):
        return self.filter(author=author)

    def contains_text(self, text):
        return self.filter(text__icontains=text)
