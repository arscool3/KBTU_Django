from django.db import models
# noinspection PyUnresolvedReferences
from api.models.category import Category

class Book(models.Model):
    def __str__(self):
        return f'{self.id}  {self.title}'
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.CharField(max_length=255)
    description = models.TextField()
    pages = models.IntegerField()
    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'category': self.category.name,
            'description': self.description,
            'pages': self.pages
        }