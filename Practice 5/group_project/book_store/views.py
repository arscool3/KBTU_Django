from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *

def get_books(request):
    books = Book.objects.all()
    data = [{'id': book.id, 'title': book.title, 'author': book.author.name} for book in books]
    return JsonResponse(data, safe=False)

def get_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    data = {'id': book.id, 'title': book.title, 'author': book.author.name, 'published_date': book.published_date}
    return JsonResponse(data)

def get_authors(request):
    authors = Author.objects.all()
    data = [{'id': author.id, 'name': author.name} for author in authors]
    return JsonResponse(data, safe=False)

def get_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    data = {'id': author.id, 'name': author.name, 'bio': author.bio}
    return JsonResponse(data)

def get_publishers(request):
    publishers = Publisher.objects.all()
    data = [{'id': publisher.id, 'name': publisher.name, 'location': publisher.location} for publisher in publishers]
    return JsonResponse(data, safe=False)

def get_publisher(request, publisher_id):
    publisher = get_object_or_404(Publisher, id=publisher_id)
    data = {'id': publisher.id, 'name': publisher.name, 'location': publisher.location}
    return JsonResponse(data)

@csrf_exempt
def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_name = request.POST.get('author')
        published_date = request.POST.get('published_date')
        
        author, created = Author.objects.get_or_create(name=author_name)
        book = Book.objects.create(title=title, author=author, published_date=published_date)
        
        data = {'id': book.id, 'title': book.title, 'author': book.author.name, 'published_date': book.published_date}
        return JsonResponse(data, status=201)
    else:
        return JsonResponse({'error': 'Only POST method allowed'}, status=405)

@csrf_exempt
def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        author_name = request.POST.get('author')
        published_date = request.POST.get('published_date')
        
        author, created = Author.objects.get_or_create(name=author_name)
        book.title = title
        book.author = author
        book.published_date = published_date
        book.save()
        
        data = {'id': book.id, 'title': book.title, 'author': book.author.name, 'published_date': book.published_date}
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Only POST method allowed'}, status=405)

@csrf_exempt
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return JsonResponse({'message': 'Book deleted successfully'})
    else:
        return JsonResponse({'error': 'Only POST method allowed'}, status=405)

@csrf_exempt
def create_author(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        bio = request.POST.get('bio')
        
        author = Author.objects.create(name=name, bio=bio)
        
        data = {'id': author.id, 'name': author.name, 'bio': author.bio}
        return JsonResponse(data, status=201)
    else:
        return JsonResponse({'error': 'Only POST method allowed'}, status=405)