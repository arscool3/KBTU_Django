from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path('home/', include('papers.urls')),
    path('<path:unknown_path>', RedirectView.as_view(url='/home/')),
]
