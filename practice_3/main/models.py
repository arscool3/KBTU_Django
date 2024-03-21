from django.db import models

class Book(models.Model):
  title = models.CharField(max_length=50)
  author = models.CharField(max_length=30)
  published_date = models.DateField()
  isbn = models.CharField(max_length=13)
  
  def __str__(self):
    return self.title
