from django.http import Http404, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from django.db.models import Max
from rest_framework.decorators import action

from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout, forms
from rest_framework.permissions import IsAuthenticated
from .forms import ProfileEditForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .tasks import send_registration_email
from .forms import RegistrationForm
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from django.shortcuts import render, get_object_or_404
from .forms import CommentForm
from .models import Trip, Category, Comment, Favorite, Order
from .serializers import TripSerializer, CategorySerializer, CommentSerializer, UserSerializer, FavoritesSerializer, FavoritesSerializer, OrderSerializer
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def home(request):
    return render(request, 'home.html', {'user': request.user})


#Authorization
def basic_form(request, given_form):
    if request.method == 'POST':
        form = given_form(data=request.POST)
        if form.is_valid():
            user = form.save()
            send_registration_email.send(user.id)  
            return redirect('login')
        else:
            raise Exception(f"some errors {form.errors}")
    return render(request, 'index.html', {'form': given_form()})

def register_view(request):
    return basic_form(request, RegistrationForm)

def logout_view(request):
    logout(request)
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        form = forms.AuthenticationForm(data=request.POST)
        if form.is_valid():
            try:
                user = authenticate(**form.cleaned_data)
                login(request, user)
                if next := request.GET.get("next"):
                    return redirect(next)
                return redirect('profile')
            except Exception:
                return HttpResponse("something is not ok")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'index.html', {'form': forms.AuthenticationForm()})


#ViewSets
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    @action(detail=False, methods=['get'])
    def most_liked_trip(self, request):
        most_liked_trip = Trip.objects.annotate(max_likes=Max('like')).order_by('-max_likes').first()

        if most_liked_trip:
            serializer = self.get_serializer(most_liked_trip)
            return Response(serializer.data)
        else:
            return Response({"message": "No trips found"}, status=status.HTTP_404_NOT_FOUND)
        
    @action(detail=False, methods=['get'])
    def by_category(self, request):
        category_id = request.query_params.get('category_id')

        if category_id:
            trips = Trip.objects.filter(category_id=category_id)
            serializer = self.get_serializer(trips, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "Please provide a category_id parameter"}, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoritesSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer




@api_view(['GET'])
def trips_list(request):
    vocuhers = Trip.objects.all()
    serializers = TripSerializer(vocuhers, many=True)
    return render(request, 'trips_list.html', {'trips_data': serializers.data})


@api_view(['GET', 'POST'])
def trips_detail(request, trip_id):
    try:
        trip = Trip.objects.get(id=trip_id)
    except Trip.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    comments = Comment.objects.filter(trip=trip)

    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.trip = trip
            comment.save()
            return redirect('trips_detail', trip_id=trip_id)
    else:
        form = CommentForm()

    serializer = TripSerializer(trip)
    return render(request, 'trips_detail.html', {'trip_data': serializer.data, 'form': form, 'comments': comments})



@api_view(['GET'])
def categories_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return render(request, 'categories_list.html', {'categories': serializer.data})

@api_view(['GET'])
def categories_trips(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    trips = Trip.objects.filter(category=category)
    serializer = TripSerializer(trips, many=True)
    return render(request, 'category_detail.html', {'category': category, 'trips': serializer.data})


@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def favorite_list(request):
    if request.method == 'GET':
        favorites = Favorite.objects.filter(user=request.user)
        serializer = FavoritesSerializer(favorites, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        user = request.user
        trip_id = request.data.get('trip_id')
        trip = Trip.objects.get(id=trip_id)

        if Favorite.objects.filter(user=user, trip=trip).exists():
            return Response({'message': 'This trip is already in favorites.'}, status=status.HTTP_400_BAD_REQUEST)
        
        Favorite.objects.create(user=user, trip=trip)
        return Response({'message': 'Trip added to favorites successfully'})
    
@login_required
@api_view(['GET', 'DELETE'])
def get_favorite_by_trip(request,id):
    if request.method == 'GET':
        trip_obj = Trip.objects.get(id=id)
        favorites_obj = Favorite.objects.filter(trip=trip_obj)
        favorites = FavoritesSerializer(favorites_obj,many=True)

        return Response(favorites.data)
    if request.method == 'DELETE':
        try:
            trip_obj = Trip.objects.get(id=id)
            favorite = Favorite.objects.filter(trip=trip_obj)
            favorite.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Favorite.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


@login_required
@api_view(['GET'])
def get_favorites_by_user(request, id):
    if request.method == 'GET':
        user = User.objects.get(id=id)
        favorites = Favorite.objects.filter(user=user)
        serializer = FavoritesSerializer(favorites, many=True)
        return Response(serializer.data)
    
@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_favorites(request):
    if request.method == 'GET':
        
        favorites = Favorite.objects.filter(user=request.user)
        return render(request, 'favorites.html', {'favorites': favorites})
    
        
class UsersListAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UsersDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(id=pk)
        except User.DoesNotExist as e:
            raise Http404

    def get(self, request, pk=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

@login_required
def create_comment(request, trip_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.trip_id = trip_id
            comment.save()
            return redirect('trips_detail', trip_id=trip_id)
    else:
        form = CommentForm()
    return render(request, 'comment_form.html', {'form': form})

class CommentsListAPIView(APIView):

    def get_objects(self, trip_id):
        try:
            return Comment.objects.filter(trip=trip_id)
        except Comment.DoesNotExist as e:
            raise Http404

    def get(self, request, trip_id=None):
        comments = self.get_objects(trip_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    def post(self, request, trip_id):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Comment.objects.get(id=pk)
        except Comment.DoesNotExist as e:
            raise Http404

    def get(self, request, trip_id=None, pk=None):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, trip_id=None, pk=None):
        comment = self.get_object(pk)
        serializer = CommentSerializer(instance=comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, trip_id=None, pk=None):
        comment = self.get_object(pk)
        comment.delete()
        return Response({'message': 'deleted'}, status=status.HTTP_204_NO_CONTENT)


@login_required
def profile(request):
    user = request.user

    if request.method == 'POST':
        profile_form = ProfileEditForm(request.POST, instance=user)
        password_form = PasswordChangeForm(user, request.POST)

        if 'profile-form' in request.POST and profile_form.is_valid():
            profile_form.save()
            return redirect('profile')
        elif 'password-form' in request.POST and password_form.is_valid():
            password_form.save()
            update_session_auth_hash(request, user)  # Updating the session after changing the password
            return redirect('profile')
    else:
        profile_form = ProfileEditForm(instance=user)
        password_form = PasswordChangeForm(user)

    return render(request, 'profile.html', {'user': user, 'profile_form': profile_form, 'password_form': password_form})

