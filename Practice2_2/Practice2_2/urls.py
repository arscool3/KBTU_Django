from django.urls import include, path
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('students/', student_list, name='student_list'),
]

urlpatterns += router.urls