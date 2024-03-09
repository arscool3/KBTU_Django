from django.shortcuts import render
from my_app.models import Favorite

def favorites(request):
    user = request.user
    favorites = Favorite.objects.filter(user=user)
    return render(request, 'favorites.html', {'favorites': favorites})
