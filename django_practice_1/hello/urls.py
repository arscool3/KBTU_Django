
from django.urls import path
from . import views
urlpatterns = [
    path("view1/",views.view1, name='view1'),
    path('view2/', views.view2, name='view2'),
    path('view3/', views.view3, name='view3')
]