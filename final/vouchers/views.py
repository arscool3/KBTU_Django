from django.http import Http404, JsonResponse
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from django.db.models import Max
from rest_framework.decorators import action
from django.db.models import Q
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout, decorators, forms
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from .forms import ProfileEditForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .tasks import send_registration_email
from .forms import RegistrationForm



from django.views import View
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


from django.shortcuts import render, get_object_or_404
from .forms import CommentForm
from .models import Voucher, Category, Comment, Favorite, Order
from .serializers import VoucherSerializer, CategorySerializer, CommentSerializer, UserSerializer, FavoritesSerializer, FavoritesSerializer, OrderSerializer
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def home(request):
    return render(request, 'home.html', {'user': request.user})


@api_view(['GET'])
def vouchers_list(request):
    vocuhers = Voucher.objects.all()
    serializers = VoucherSerializer(vocuhers, many=True)
    return render(request, 'vouchers_list.html', {'vouchers_data': serializers.data})


@api_view(['GET', 'POST'])
def vouchers_detail(request, voucher_id):
    try:
        voucher = Voucher.objects.get(id=voucher_id)
    except Voucher.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    comments = Comment.objects.filter(voucher=voucher)

    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.voucher = voucher
            comment.save()
            return redirect('vouchers_detail', voucher_id=voucher_id)
    else:
        form = CommentForm()

    serializer = VoucherSerializer(voucher)
    return render(request, 'vouchers_detail.html', {'voucher_data': serializer.data, 'form': form, 'comments': comments})



@api_view(['GET'])
def categories_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return render(request, 'categories_list.html', {'categories': serializer.data})

@api_view(['GET'])
def categories_vouchers(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    vouchers = Voucher.objects.filter(category=category)
    serializer = VoucherSerializer(vouchers, many=True)
    return render(request, 'category_detail.html', {'category': category, 'vouchers': serializer.data})


@api_view(['GET', 'POST'])
def favorite_list(request):
    if request.method == 'GET':
        favorites = Favorite.objects.all()
        serializer = FavoritesSerializer(favorites, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = FavoritesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def get_favorite_by_voucher(request,id):
    if request.method == 'GET':
        voucher_obj = Voucher.objects.get(id=id)
        favorites_obj = Favorite.objects.filter(voucher=voucher_obj)
        favorites = FavoritesSerializer(favorites_obj,many=True)

        return Response(favorites.data)
    if request.method == 'DELETE':
        try:
            voucher_obj = Voucher.objects.get(id=id)
            favorite = Favorite.objects.filter(voucher=voucher_obj)
            favorite.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Favorite.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


@login_required
@api_view(['GET'])
def get_favorites_by_user(request,id):
    if request.method == 'GET':
        user_obj = User.objects.get(id=id)
        favorites_obj = Favorite.objects.filter(user=user_obj)
        favorites = FavoritesSerializer(favorites_obj,many=True)

        return Response(favorites.data)


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
def create_comment(request, voucher_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.voucher_id = voucher_id
            comment.save()
            return redirect('vouchers_detail', voucher_id=voucher_id)
    else:
        form = CommentForm()
    return render(request, 'comment_form.html', {'form': form})

class CommentsListAPIView(APIView):

    def get_objects(self, voucher_id):
        try:
            return Comment.objects.filter(voucher=voucher_id)
        except Comment.DoesNotExist as e:
            raise Http404

    def get(self, request, voucher_id=None):
        comments = self.get_objects(voucher_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    def post(self, request, voucher_id):
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

    def get(self, request, voucher_id=None, pk=None):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, voucher_id=None, pk=None):
        comment = self.get_object(pk)
        serializer = CommentSerializer(instance=comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, voucher_id=None, pk=None):
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
            update_session_auth_hash(request, user)  # Обновление сессии после изменения пароля
            return redirect('profile')
    else:
        profile_form = ProfileEditForm(instance=user)
        password_form = PasswordChangeForm(user)

    return render(request, 'profile.html', {'user': user, 'profile_form': profile_form, 'password_form': password_form})


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class VoucherViewSet(viewsets.ModelViewSet):
    queryset = Voucher.objects.all()
    serializer_class = VoucherSerializer

    @action(detail=False, methods=['get'])
    def most_liked_voucher(self, request):
        most_liked_voucher = Voucher.objects.annotate(max_likes=Max('like')).order_by('-max_likes').first()

        if most_liked_voucher:
            serializer = self.get_serializer(most_liked_voucher)
            return Response(serializer.data)
        else:
            return Response({"message": "No vouchers found"}, status=status.HTTP_404_NOT_FOUND)
        
    @action(detail=False, methods=['get'])
    def by_category(self, request):
        category_id = request.query_params.get('category_id')

        if category_id:
            vouchers = Voucher.objects.filter(category_id=category_id)
            serializer = self.get_serializer(vouchers, many=True)
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