from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from my_app.models import Book, Order, Author, Genre
from django.shortcuts import render


def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author_id')
        genre_id = request.POST.get('genre_id')
        price = request.POST.get('price')
        
        author = get_object_or_404(Author, id=author_id)
        genre = get_object_or_404(Genre, id=genre_id)
        
        book = Book.objects.create(title=title, author=author, genre=genre, price=price)
        return JsonResponse({'message': 'Book created successfully'})

def get_books(request):
    if request.method == 'GET':
        books = Book.objects.all()
        data = {'books': list(books.values())}
        return JsonResponse(data)

def create_order(request):
    if request.method == 'POST':
        book_ids = request.POST.getlist('book_ids[]')
        total_price = request.POST.get('total_price')
        
        books = Book.objects.filter(id__in=book_ids)
        
        order = Order.objects.create(total_price=total_price)
        order.books.set(books)
        return JsonResponse({'message': 'Order created successfully'})

def get_orders(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        data = {'orders': list(orders.values())}
        return JsonResponse(data)

def get_book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})

def get_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order_detail.html', {'order': order})