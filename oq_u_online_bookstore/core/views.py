from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, decorators, logout, forms
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.urls import reverse
from .forms import BookForm, AuthorForm, GenreForm, OrderForm, ReviewForm
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from .models import Book, BookDetail, UserProfile, Author, Genre, Review, Order

# GET Methods

def get_user_profile(user_id):
    # Retrieve the profile of a specific user
    user = User.objects.get(pk=user_id)
    return UserProfile.objects.get(user=user)

def get_book_detail(book_id):
    # Retrieve the details of a specific book
    book = Book.objects.get(pk=book_id)
    return BookDetail.objects.get(book=book)


def get_all_books(request):
    books = Book.objects.all()
    return render(request, 'books_list.html', {'books': books})

def get_all_authors(request):
    authors = Author.objects.all()
    return render(request, 'authors_list.html', {'authors': authors})

def get_all_genres(request):
    genres = Genre.objects.all()
    return render(request, 'genres_list.html', {'genres': genres})


def get_books_by_author(author_id):
    # Retrieve all books written by a specific author
    author = Author.objects.get(pk=author_id)
    return author.books.all()

def get_list_of_books_by_genre(genre_id):
    # Retrieve all books belonging to a specific genre
    genre = Genre.objects.get(pk=genre_id)
    return genre.books.all()

def books_by_genre(request, genre_id):
    genre = get_object_or_404(Genre, pk=genre_id)
    books = Book.objects.by_genre(genre_id)
    return render(request, 'books_by_genre.html', {'genre': genre, 'books': books})

def books_by_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    books = Book.objects.by_author(author_id)
    return render(request, 'books_by_author.html', {'author': author, 'books': books})

# def books_by_genre(request, genre_id):
#     # Retrieve the Genre object based on the genre_id, or return a 404 error if not found
#     genre = get_object_or_404(Genre, id=genre_id)
    
#     # Log or print the value of genre to ensure it's a single instance
#     print("Genre:", genre)

#     # Filter books by the retrieved Genre object
#     books = Book.objects.filter(genre=genre)
    
#     # Pass the filtered books queryset and the genre object to the template
#     return render(request, 'core/books_by_genre.html', {'books': books, 'genre': genre})

def get_user_orders(user_id):
    # Retrieve all orders placed by a specific user
    user = User.objects.get(pk=user_id)
    return user.order_set.all()

def get_reviews_for_book(book_id):
    # Retrieve all reviews for a specific book
    book = Book.objects.get(pk=book_id)
    return book.review_set.all()


# POST Methods

def post_new_book(title, author_ids, genre_ids, description, publication_date):
    # Create a new book with the given details
    new_book = Book.objects.create(
        title=title,
        description=description,
        publication_date=publication_date
    )
    new_book.author.add(*author_ids)
    new_book.genre.add(*genre_ids)
    new_book.save()

def post_new_author(name, biography, nationality):
    # Create a new author with the given details
    new_author = Author.objects.create(
        name=name,
        biography=biography,
        nationality=nationality
    )

def post_new_genre(name):
    # Create a new genre with the given name
    new_genre = Genre.objects.create(name=name)

def post_new_order(user_id, book_ids, total_price, shipping_address, status):
    # Create a new order with the given details
    user = User.objects.get(pk=user_id)
    new_order = Order.objects.create(
        user=user,
        total_price=total_price,
        shipping_address=shipping_address,
        status=status
    )
    new_order.books.add(*book_ids)
    new_order.save()

def post_new_review(user_id, book_id, rating, review_text):
    # Create a new review for a book by the given user
    user = User.objects.get(pk=user_id)
    book = Book.objects.get(pk=book_id)
    new_review = Review.objects.create(
        user=user,
        book=book,
        rating=rating,
        review_text=review_text
    )

def post_new_user_profile(user_id, address, contact_number):
    # Create a new user profile for the given user
    user = User.objects.get(pk=user_id)
    UserProfile.objects.create(
        user=user,
        address=address,
        contact_number=contact_number
    )

def post_new_book_detail(book_id, pages, isbn):
    # Create new book details for the given book
    book = Book.objects.get(pk=book_id)
    BookDetail.objects.create(
        book=book,
        pages=pages,
        isbn=isbn
    )


def home(request):
    # Logic to fetch data from models can be included here if needed
    return render(request, 'home.html')  # Assuming your homepage template is named 'home.html'

def create_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home page after successfully registering the user
    else:
        form = UserRegistrationForm()
    return render(request, 'create_user.html', {'form': form})

# for our forms
@decorators.login_required(login_url='login')
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home page after successfully creating a book
    else:
        form = BookForm()
    return render(request, 'create_book.html', {'form': form})

@decorators.login_required(login_url='login')
def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home page after successfully creating a book
    else:
        form = AuthorForm()
    return render(request, 'create_author.html', {'form': form})

@decorators.login_required(login_url='login')
def create_genre(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home page after successfully creating a book
    else:
        form = GenreForm()
    return render(request, 'create_genre.html', {'form': form})

@decorators.login_required(login_url='login')
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home page after successfully creating a book
    else:
        form = OrderForm()
    return render(request, 'create_order.html', {'form': form})

@decorators.login_required(login_url='login')
def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home page after successfully creating a book
    else:
        form = ReviewForm()
    return render(request, 'create_review.html', {'form': form})


def basic_form(request, given_form):
    if request.method == 'POST':
        form = given_form(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("OK")
        else:
            # Form is invalid, render login page with form and errors
            return render(request, 'registration.html', {'form': form})
    return render(request, 'registration.html', {'form': given_form()})


def register_view(request):
    return basic_form(request, forms.UserCreationForm)

def logout_view(request):
    logout(request)
    return HttpResponse("You have logged out succesfully.")


def login_view(request):
    if request.method == 'POST':
        form = forms.AuthenticationForm(data=request.POST)
        if form.is_valid():
            try:
                user = authenticate(**form.cleaned_data)
                login(request, user)
                if next := request.GET.get("next"):
                    return redirect(next)
                return HttpResponse("everything is ok")
            except Exception:
                return HttpResponse("something is not ok")
        else:
            # Form is invalid, render login page with form and errors
            return render(request, 'login.html', {'form': form})
    return render(request, 'login.html', {'form': forms.AuthenticationForm()})





