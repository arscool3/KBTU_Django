from django.db import models

# 1. User Model
from django.contrib.auth.models import User

# This model represents the user authentication and profile management.
# It uses Django's built-in User model.
# Additional profile information can be stored by extending the User model if needed.

# No explicit model definition is required for the User model.


from django.db import models
from django.contrib.auth.models import User

#1.2  User Profile Model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    contact_number = models.CharField(max_length=20)
    # Add any other fields you want to include in the user profile

    def __str__(self):
        return f"Profile of {self.user.username}"

# 2.2 Book Detail Model
class BookDetail(models.Model):
    book = models.OneToOneField('Book', on_delete=models.CASCADE)
    pages = models.IntegerField()
    isbn = models.CharField(max_length=20)
    # Add any other fields specific to book details

    def __str__(self):
        return f"Details of '{self.book.title}'"


# 2.1 Book model
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ManyToManyField('Author', related_name='books')
    genre = models.ManyToManyField('Genre', related_name='books')
    description = models.TextField()
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

    #Book model has a ManyToMany relationship with the Author model,
    #  indicating that each book can have multiple authors and each author can have written multiple books. 

    #Book model has a ManyToMany relationship with the Genre model,
    #  signifying that each book can belong to multiple genres and each genre can have multiple associated books.
  

# 3. Author Model
class Author(models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField()
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# 4. Genre Model
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# 5. Order Model
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #Order model has a ForeignKey relationship with the User model, representing the fact that one user can have multiple orders. 
    books = models.ManyToManyField('Book', related_name='orders')
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.IntegerField()
    shipping_address = models.TextField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return f"Order #{self.pk} by {self.user.username}"


# 6. Review Model
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review of '{self.book.title}' by {self.user.username}"

