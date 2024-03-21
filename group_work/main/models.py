from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    destinations = models.ManyToManyField(Destination, related_name='articles')

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50)
    articles = models.ManyToManyField(Article, related_name='tags')
    def __str__(self):
        return self.name