from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import upload_novel, bookmark_chapter, add_chapter, register, user_login, user_logout, add_review, \
    search_results

urlpatterns = [
                  # GET Requests
                  path('', views.home, name='home'),
                  path('novels/<int:novel_id>/', views.novel_detail, name='novel_detail'),
                  path('novels/<int:novel_id>/chapters/<int:chapter_id>/', views.chapter_reading,
                       name='chapter_reading'),
                  path('user/<int:user_id>/profile/', views.user_profile, name='user_profile'),
                  path('bookmarks/', views.my_bookmarks, name='my_bookmarks'),
                  path('upload_novel/', upload_novel, name='upload_novel'),
                  path('bookmark_chapter/<int:novel_id>/<int:chapter_id>/', bookmark_chapter, name='bookmark_chapter'),
                  path('novels/<int:novel_id>/add_chapter/', add_chapter, name='add_chapter'),
                  path('register/', register, name='register'),
                  path('login/', user_login, name='login'),
                  path('logout/', user_logout, name='logout'),
                  path('add_review/<int:novel_id>/', add_review, name='add_review'),
                  path('search/', search_results, name='search_results'),
                  # # POST Requests
                  # path('novels/<int:novel_id>/reviews/new/', views.submit_review, name='submit_review'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
