from django.urls import path
from .views import CategoryListView, TagListView, PostListView, CommentListView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('tags/', TagListView.as_view(), name='tag_list'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('comments/', CommentListView.as_view(), name='comment_list'),
]
