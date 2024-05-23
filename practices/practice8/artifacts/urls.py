from django.urls import path
from .views import ArtifactListCreate, ArtifactRetrieveUpdateDestroy

urlpatterns = [
    path('artifacts/', ArtifactListCreate.as_view()),
    path('artifacts/<int:pk>/', ArtifactRetrieveUpdateDestroy.as_view()),
]