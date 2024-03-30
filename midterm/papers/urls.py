from django.urls import path
from .views import *
from comments.views import add_comment

urlpatterns = [
    path('', home, name='home'),
    path('papers-by-category/<int:category_id>/', papers_by_category, name='papers_by_category'),
    path('papers/<int:paper_id>/', paper_detail, name='paper_detail'),
    path('add_to_shelf/<int:paper_id>/', add_to_shelf, name='add_to_shelf'),
    path('create_paper/', create_paper, name='create_paper'),
    path('add_comment/<int:paper_id>/', add_comment, name='add_comment'),
    path('create_tag/', create_tag, name='create_tag'),
    path('create_category/', create_category, name='create_category'),
    path('search_by_tags/',search_by_tags, name='search_by_tags'),
    path('drf_papers', PaperListView.as_view(), name='drf_paper'),
    path('drf_papers/<int:pk>/', PaperRetrieveUpdateDestroyView.as_view(), name='drf_paper_detail'),
]


