from django.urls import path
from . import views

urlpatterns=[
    path('get_articles_api',views.getArticles),
    path('add_articles_api',views.addArticles),
    path('del_articles_api',views.delArticles),
    path('upd_articles_api',views.updArticles),

    path('get_topics_api',views.getTopics),
    path('add_topics_api',views.addTopics),
    path('del_topics_api',views.delTopics),
    path('upd_topics_api',views.updTopics),
    

    path('get_profiles_api',views.getProfiles),
    path('get_follows_api',views.getFollows),
    path('get_comments_api',views.getComments),
    path('get_likes_api',views.getLikes),
    path('get_readinglists_api',views.getReadingLists),

]