from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from .models import Author, Book
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Book, Review
from .forms import ReviewForm
from django.urls import reverse_lazy


def home(request):
    search_query = request.GET.get('search', '')
    genre_query = request.GET.get('genre', '')
    
    if search_query:
        books = Book.objects.filter(title__icontains=search_query) | Book.objects.filter(author__name__icontains=search_query)
    else:
        books = Book.objects.all()
    
    if genre_query:
        books = books.filter(genre__iexact=genre_query)
    
    genres = Book.objects.values_list('genre', flat=True).distinct()
    return render(request, 'books/home.html', {'books': books, 'genres': genres, 'selected_genre': genre_query})


# List all books
class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'books/book_list.html'

# View a single book detail
class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'

# List all authors
class AuthorListView(ListView):
    model = Author
    context_object_name = 'authors'
    template_name = 'books/author_list.html'

# View books by an author
class BooksByAuthorView(ListView):
    model = Book
    template_name = 'books/books_by_author.html'
    context_object_name = 'books'


class CreateBookReviewView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'books/add_review.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.book = get_object_or_404(Book, pk=self.kwargs['book_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('book-detail', kwargs={'pk': self.kwargs['book_id']})
