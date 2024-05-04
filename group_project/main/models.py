from django.db import models

# Create your models here.

class Base(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name




class Author(Base):
    age = models.IntegerField()




class BookQuerySet(models.QuerySet):
    def get_books_by_authors_id(self, name_id:str):
        #it is filtered by author id
        return self.filter(author_name = name_id)
    
    def order_books_by_price(self):
        return self.order_by('price')
    
    def get_by_genres(self, genre_name):
        return self.filter(genre = genre_name)
    
    def order_books_by_year(self):
        return self.order_by('year_of_publication')


class Book(Base):
    genre = models.CharField(max_length=30)
    price = models.FloatField()
    year_of_publication = models.DateField()
    author_name = models.ForeignKey(Author, on_delete = models.DO_NOTHING)
    objects = BookQuerySet.as_manager()


    
class LibraryQuerySet(models.QuerySet):
    def get_all_matched_books(self, book_name):
        return self.filter(books__name = book_name)
    
    def get_locations(self, city):
        return self.filter(location = city)


class Library(Base):
    books = models.ManyToManyField("Book", related_name="books")
    location = models.TextField()
    objects = LibraryQuerySet.as_manager()

class Client(Base):
    cart = models.ManyToManyField("Book", related_name="ordered_books")