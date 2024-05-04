from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Book, Category, Order, Review

def user_list(request):
    if request.user.is_superuser:  # Check if user is admin
        users = User.objects.all()
        return render(request, 'bookstore/user_list.html', {'users': users})
    else:
        return HttpResponseForbidden("You are not authorized to view this page.")

def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookstore/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'bookstore/book_detail.html', {'book': book})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'bookstore/category_list.html', {'categories': categories})

def order_list(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(user=request.user)
        return render(request, 'bookstore/order_list.html', {'orders': orders})
    else:
        return HttpResponseForbidden("You must be logged in to view your orders.")

def review_list(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = book.reviews.all()
    return render(request, 'bookstore/review_list.html', {'book': book, 'reviews': reviews})


# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import BookForm, CategoryForm, OrderForm, ReviewForm

def user_create(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = UserCreationForm()
    return render(request, 'bookstore/user_create.html', {'form': form})

@login_required
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to book list page after successful creation
    else:
        form = BookForm()
    return render(request, 'bookstore/book_create.html', {'form': form})

@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')  # Redirect to category list page after successful creation
    else:
        form = CategoryForm()
    return render(request, 'bookstore/category_create.html', {'form': form})

@login_required
def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('order_list')  
    else:
        form = OrderForm()
    return render(request, 'bookstore/order_create.html', {'form': form})

@login_required
def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('book_detail', pk=review.book.pk)  # Redirect to book detail page after successful creation
    else:
        form = ReviewForm()
    return render(request, 'bookstore/review_create.html', {'form': form})
