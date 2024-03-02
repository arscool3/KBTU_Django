from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .models import Book, Author, Genre, User, BorrowedBooks, Review

def book_list(request):
    genre_filter = request.GET.get('genre')
    author_filter = request.GET.get('author')

    books = Book.objects.all()
    if genre_filter:
        books = books.filter(genre__name=genre_filter)
    if author_filter:
        books = books.filter(author__name=author_filter)

    return render(request, 'book_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    reviews = Review.objects.filter(book=book)
    return render(request, 'book_detail.html', {'book': book, 'reviews': reviews})

def user_profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'user_profile.html', {'user': user})

@require_POST
def borrow_book(request):
    user_id = request.POST.get('user_id')
    book_id = request.POST.get('book_id')

    user = get_object_or_404(User, pk=user_id)
    book = get_object_or_404(Book, pk=book_id)

    if user.borrowed_books.count() == 0:
        borrowed_book = BorrowedBooks.objects.create(user=user, book=book)
        return JsonResponse({'status': 'success', 'message': 'Book borrowed successfully.'})
    else:
        return JsonResponse({'status': 'error', 'message': 'User can only borrow one book at a time.'})

@require_POST
def add_review(request):
    user_id = request.POST.get('user_id')
    book_id = request.POST.get('book_id')
    rating = request.POST.get('rating')
    comments = request.POST.get('comments')

    user = get_object_or_404(User, pk=user_id)
    book = get_object_or_404(Book, pk=book_id)

    review, created = Review.objects.get_or_create(user=user, book=book, defaults={'rating': rating, 'comments': comments})

    if not created:
        review.rating = rating
        review.comments = comments
        review.save()

    return JsonResponse({'status': 'success', 'message': 'Review added successfully.'})
