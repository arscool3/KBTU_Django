from rest_framework import viewsets
from .models import Location, Tour, Review, Request, Rating
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
from .serializers import LocationSerializer, TourSerializer, ReviewSerializer, RequestSerializer, UserSerializer, \
    RatingSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from .tasks import send_email, test
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.

def tour_list(request):
    tours = Tour.objects.all()
    test.send("gege")

    name_filter = request.GET.get('name')
    if name_filter:
        tours = tours.filter(name__icontains=name_filter)

    price_filter = request.GET.get('price')
    if price_filter:
        try:
            price_filter = float(price_filter)
            tours = tours.filter(price__lte=price_filter)
        except ValueError:
            pass

    return render(request, 'tour_list.html', {'tours': tours})


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['get'])
    def increase_price(self, request, pk=None):
        tour = self.get_object()
        # Increase the price of the tour by 10%
        new_price = tour.price * 1.1
        # pipeline(send_email.send(to='admin@example.com', subject='Price Increased',
        #                          body=f"The price of tour {tour.name} has been increased to ${new_price}."))
        test.send("book")
        tour.price = new_price
        tour.save()
        return Response({'detail': 'Price increased by 10%'})

    @action(detail=False, methods=['get'])
    def cheap_tours(self, request):
        # Retrieve tours with prices less than $100
        cheap_tours = self.queryset.filter(price__lt=100)
        serializer = self.get_serializer(cheap_tours, many=True)
        return Response(serializer.data)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = (IsOwnerOrReadOnly,)


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
