from django.urls import path
from main import views

urlpatterns = [
  # path('', index, name='index'),
  # path('login/', login_view, name='login'),
  # path("logout/", logout_view, name='logout'),
  
  # GET endpoints
  path('users/', views.UserListView().as_view(), name='users'),
  path('authors/', views.AuthorListView().as_view(), name='authors'),
  path('categories/', views.CategoryListView().as_view(), name='categories'),
  path('books/', views.BookListView().as_view(), name='books'),
  path('books/<int:id>', views.BookDetailView().as_view(), name='get_book'),
  path('consumers/', views.ConsumerListView().as_view(), name='consumers'),
  path('reviews/', views.ReviewListView().as_view(), name='reviews'),
  
  # POST endpoints
  path('users/add/', views.RegisterUserView().as_view()),
  path('authors/add/', views.AddAuthorView().as_view()),
  path('categories/add', views.AddCategoryView().as_view()),
  path('books/add/', views.AddBookView().as_view()),
  path('consumers/add/', views.AddConsumerView().as_view()),
  path('reviews/add/', views.AddReviewView().as_view()),
]