from django.db import models
from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length= 70)
    
    class Meta:
        abstract = True

    def __str__(self):
        return self.name 
    
#Student - book - one_to_many
#teacher - student - many to many


# custom_queryset.py


class StudentQuerySet(models.QuerySet):
    def with_more_books_than(self, count):
        return self.annotate(book_count=models.Count('book')).filter(book_count__gt=count)
    
    def order_by_book_count(self):
        return super().order_by('-book_count')
        
    
class Student(Person):
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    book_count = models.IntegerField(default=0)    
    Students = StudentQuerySet.as_manager()



    
class BookQuerySet(models.QuerySet):
    def ebooks(self):
        return self.filter(online_version_exists=True)

    def paper_books(self):
        return self.filter(online_version_exists=False)
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    online_version_exists= models.BooleanField(default=False)
    students = models.ForeignKey('Student', on_delete=models.CASCADE, related_name= 'books')
    Books = BookQuerySet.as_manager()

    def __str__(self):
        return self.title
    
class Admin(Person):
    pass
class Teacher(Person):
    # years_of_experience = models.IntegerField
    students = models.ManyToManyField('Student')

# class TeacherQuerySet(models.QuerySet):
