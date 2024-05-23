from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TagViewSet, QuestionViewSet, AnswerViewSet, VoteViewSet, CommentViewSet, question_detail, questions_list, create_question, create_answer, create_tag, signin, signup, home, user_logout, welcome, should_login, add_view
from rest_framework.authtoken import views


router = DefaultRouter()
router.register(r'tags', TagViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)
router.register(r'votes', VoteViewSet)
router.register(r'comments', CommentViewSet)


urlpatterns = [
    path('', welcome, name='welcome'),
    path('home/', home, name='home'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout/', user_logout, name='logout'),
    path('tags/create/', create_tag, name='create_tag'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('should_login/', should_login, name='should_login'),
    path('questions/', questions_list, name='questions_list'),
    path('questions/create/', create_question, name='create_question'),
    path('questions/<int:question_id>/', question_detail, name='question_detail'),
    path('questions/<int:question_id>/answer/', create_answer, name='create_answer'),
    path('questions/<int:pk>/upvote/', QuestionViewSet.as_view({'post': 'upvote'}), name='question-upvote'),
    path('questions/<int:pk>/downvote/', QuestionViewSet.as_view({'post': 'downvote'}), name='question-downvote'),
    path('answers/<int:pk>/upvote/', AnswerViewSet.as_view({'post': 'upvote'}), name='answer-upvote'),
    path('answers/<int:pk>/downvote/', AnswerViewSet.as_view({'post': 'downvote'}), name='answer-downvote'),
    path('', include(router.urls)),

    path('add_view/', add_view, name='celery')
]


urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token)
]
