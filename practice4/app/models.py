from django.db import models


class BookstoreClerk(models.Manager):
    def aggregate_books_by_genre(self):
        aggregated_books = {}  
        # Retrieve all distinct genres present in the database
        genres = self.distinct('genre').values_list('genre', flat=True)   
        # Iterate over each genre
        for genre in genres:
            # Filter books by genre and sort them alphabetically by title
            books_in_genre = self.filter(genre=genre).order_by('title')
            # Store the sorted list of books for the genre
            aggregated_books[genre] = list(books_in_genre)
        return aggregated_books
    
    def  update_book_prices(self, percentage_increase):
        # Calculate the new prices based on the percentage increase
        new_prices = models.F('price') * (1 + percentage_increase / 100)

        updated_books = self.update(price=new_prices)
        return updated_books

class Consultant(models.Manager):
    def get_author(self):
        return super().get_queryset().filter(author="Dan Brown")
    def give_reading_recs(self):
        return super().get_queryset().exclude(genre='Horror Stories')
    
class Base(models.Model):
    name = models.CharField(max_length=20,default='default')

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Author(Base):
    pass
class Book(Base):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre=models.CharField(max_length=100)
    objects = Consultant(),BookstoreClerk()
    price=models.IntegerField()

class Publisher(Base):
    pass

class Magazine(Base):
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    price=models.IntegerField()
"""
author1 = Author.objects.create(name="John Smith")
author2 = Author.objects.create(name="Jane Doe")

# Populate the Publisher model
publisher1 = Publisher.objects.create(name="Publisher X")
publisher2 = Publisher.objects.create(name="Publisher Y")

# Populate the Book model
book1 = Book.objects.create(title="Book 1", author=author1, genre="Fiction", price=20)
book2 = Book.objects.create(title="Book 2", author=author1, genre="Non-fiction", price=25)
book3 = Book.objects.create(title="Book 3", author=author2, genre="Horror Stories", price=30)
book4 = Book.objects.create(title="Book 4", author=author2, genre="Fantasy", price=22)

# Populate the Magazine model
magazine1 = Magazine.objects.create(title="Magazine 1", publisher=publisher1, price=5)
magazine2 = Magazine.objects.create(title="Magazine 2", publisher=publisher2, price=6)
magazine3 = Magazine.objects.create(title="Magazine 3", publisher=publisher1, price=4)

"""
