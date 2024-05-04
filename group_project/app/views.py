from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Book, Author, Publisher, Review
import json

# GET View for Books
def book_list(request):
    if request.method == 'GET':
        books = list(Book.objects.values())
        return JsonResponse(books, safe=False)

# POST View for creating a Book
@csrf_exempt  # This decorator bypasses CSRF token requirement for simplicity
def create_book(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        book = Book.objects.create(name=data['name'], description=data['description'])
        return JsonResponse({"id": book.id, "name": book.name, "description": book.description})

# GET View for Authors
def author_list(request):
    if request.method == 'GET':
        authors = list(Author.objects.values())
        return JsonResponse(authors, safe=False)

# POST View for creating an Author
@csrf_exempt
def create_author(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        author = Author.objects.create(name=data['name'])
        return JsonResponse({"id": author.id, "name": author.name})
    
@csrf_exempt
def create_publisher(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        publisher = Publisher.objects.create(name=data['name'])
        return JsonResponse({"id": publisher.id, "name": publisher.name})

@csrf_exempt
def create_review(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            book_id = data.get('book_id')
            review_text = data.get('review_text')
            rating = data.get('rating', 1)  
            
            book = Book.objects.get(id=book_id)
            review = Review.objects.create(book=book, review_text=review_text, rating=rating)
            return JsonResponse({"id": review.id, "book": book_id, "review_text": review_text, "rating": rating})
        except Book.DoesNotExist:
            return HttpResponse(status=404)
        except Exception as e:
            return HttpResponse(status=400, content=str(e))
        

# Function to get all publishers
def get_publishers(request):
    if request.method == 'GET':
        publishers = list(Publisher.objects.values('id', 'name', 'location'))
        return JsonResponse(publishers, safe=False)

# Function to get all reviews for a specific book
def get_reviews(request, book_id):
    if request.method == 'GET':
        try:
            # Filter reviews by book_id, note that `reviews` is accessed via the related name from Book model
            book = Book.objects.get(id=book_id)
            reviews = book.reviews.all().values('id', 'review_text', 'rating')
            return JsonResponse(list(reviews), safe=False)
        except Book.DoesNotExist:
            return JsonResponse({'error': 'Book not found'}, status=404)


def get_books_by_author(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        author_name = data.get('author_name')
        books_by_author = Book.objects.by_author(author_name)

         # Serialize the books for JSON response
        books_data = list(books_by_author.values('id', 'name', 'description', 'author_id', 'publisher_id'))
        
        # Return the serialized books data as JSON
        return JsonResponse({'books': books_data})
    

def get_high_rated_reviews(request):
    # Get all reviews with a rating higher than 4
    high_rated_reviews = Review.objects.high_rating(4)
    return JsonResponse(list(high_rated_reviews), safe=False)
    
