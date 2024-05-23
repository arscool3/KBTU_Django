from rest_framework import viewsets
from .models import Author, Publisher, Category, Book, Member, Borrow
from .serializers import AuthorSerializer, PublisherSerializer, CategorySerializer, BookSerializer, MemberSerializer, BorrowSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
import datetime
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from .filters import BookFilter
from .tasks import update_book_availability


def home(request):
    return render(request, 'library/home.html')


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter

    @action(detail=True, methods=['get'])
    def borrowed(self, request, pk=None):
        book = self.get_object()
        borrows = Borrow.objects.filter(book=book)
        return Response({'borrowed': len(borrows) > 0})

    @action(detail=False, methods=['get'])
    def published_last_year(self, request):
        last_year = datetime.date.today().year - 1
        books = Book.objects.filter(publication_date__year=last_year)
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class BorrowViewSet(viewsets.ModelViewSet):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer

    def perform_create(self, serializer):
        borrow = serializer.save()
        update_book_availability.send(borrow.book.id)
