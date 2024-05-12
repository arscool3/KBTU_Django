from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.create_test_item),
    path('test/<int:pk>/', views.get_test_item),
    path('test/<int:pk>/update/', views.update_test_item),
    path('test/<int:pk>/delete/', views.delete_test_item),
    path('tests/', views.get_all_test_items),
]
