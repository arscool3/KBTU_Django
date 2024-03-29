
from django.urls import path

from hw.views import main, basic, test

urlpatterns = [
   path('main/', main),
   path('basic/', basic),
   path('test/', test),
]
