from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse
from .models import Book, BorrowedBook, BorrowerProfile
from .decorators import staff_required


def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'library/book_detail.html', {'book': book})

@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    borrower_profile, created = BorrowerProfile.objects.get_or_create(user=request.user)
    borrowed_book, created = BorrowedBook.objects.get_or_create(book=book, borrower=borrower_profile)
    # Additional logic for due date assignment
    return HttpResponseRedirect(reverse('book_list'))
@login_required
def return_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    borrower_profile = BorrowerProfile.objects.get(user=request.user)
    borrowed_book = BorrowedBook.objects.get(book=book, borrower=borrower_profile)
    borrowed_book.delete()
    return HttpResponseRedirect(reverse('book_list'))

@login_required
def user_profile(request):
    borrower_profile, created = BorrowerProfile.objects.get_or_create(user=request.user)
    borrowed_books = BorrowedBook.objects.filter(borrower=borrower_profile)
    return render(request, 'library/user_profile.html', {'borrowed_books': borrowed_books})

@login_required
def update_profile(request):
    if request.method == 'POST':
        # Logic for updating user profile
        return HttpResponseRedirect(reverse('user_profile'))
    else:
        return render(request, 'library/update_profile.html')
    
def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/templates/library/book_list.html', {'books': books})

def update_profile(request):
    if request.method == 'POST':
        # Logic for updating user profile
        return HttpResponseRedirect(reverse('user_profile'))
    else:
        return render(request, 'library/update_profile.html')