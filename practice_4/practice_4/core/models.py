from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    objects = models.Manager() # Default manager
    custom_manager = models.Manager() # Custom manager

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()

    objects = models.Manager() # Default manager
    custom_manager = models.Manager() # Custom manager

    def __str__(self):
        return self.title

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    objects = models.Manager() # Default manager
    custom_manager = models.Manager() # Custom manager

    def __str__(self):
        return self.name

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    objects = models.Manager() # Default manager
    custom_manager = models.Manager() # Custom manager

    def __str__(self):
        return f"{self.book.title} - {self.rating}"
