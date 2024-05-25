from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, request, HttpResponseRedirect
from .forms import NovelUploadForm, ChapterForm, ReviewForm
from .forms import UserRegistrationForm, UserProfileForm
from django.contrib.auth import authenticate, login
from .forms import UserLoginForm
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import NovelUploadForm
from .models import UserProfile, Novel, Chapter, Review, Bookmark
from .serializers import UserProfileSerializer, NovelSerializer, ChapterSerializer, ReviewSerializer, BookmarkSerializer
from .tasks import send_new_novel_notification
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class NovelViewSet(viewsets.ModelViewSet):
    queryset = Novel.objects.all()
    serializer_class = NovelSerializer

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def mark_as_favorite(self, request, pk=None):
        novel = self.get_object()
        user_profile = request.user.profile
        user_profile.favorites.add(novel)  # Ensure this is correct based on your UserProfile model
        user_profile.save()
        return Response({'status': 'novel marked as favorite'})

    @action(detail=False, methods=['get'])
    def top_rated(self, request):
        top_rated_novels = Novel.objects.order_by('-rating')[:10]  # Ensure `rating` is a field in your Novel model
        serializer = self.get_serializer(top_rated_novels, many=True)
        return Response(serializer.data)


class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer




def user_logout(request):
    logout(request)
    return redirect('home')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')
    else:
        user_form = UserRegistrationForm()
        profile_form = UserProfileForm()
    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form})


def home(request):
    novels = Novel.objects.all()
    return render(request, 'home.html', {'novels': novels})


def novel_detail(request, novel_id):
    novel = get_object_or_404(Novel, id=novel_id)
    reviews = Review.objects.filter(novel=novel)
    context = {
        'novel': novel,
        'reviews': reviews,
    }
    return render(request, 'novel_detail.html', context)


def chapter_reading(request, novel_id, chapter_id):
    chapter = get_object_or_404(Chapter, novel_id=novel_id, id=chapter_id)
    try:
        prev_chapter = Chapter.objects.filter(novel_id=novel_id, chapter_number__lt=chapter.chapter_number).order_by(
            '-chapter_number').first()
    except Chapter.DoesNotExist:
        prev_chapter = None

    try:
        next_chapter = Chapter.objects.filter(novel_id=novel_id, chapter_number__gt=chapter.chapter_number).order_by(
            'chapter_number').first()
    except Chapter.DoesNotExist:
        next_chapter = None

    context = {
        'chapter': chapter,
        'prev_chapter': prev_chapter,
        'next_chapter': next_chapter,
    }

    return render(request, 'chapter_reading.html', context)


def user_profile(request, user_id):
    user_profile = get_object_or_404(UserProfile, user_id=user_id)
    return render(request, 'user_profile.html', {'user_profile': user_profile})


# Review Page - form
@login_required
def new_review(request, novel_id):
    return render(request, 'new_review.html')


def my_bookmarks(request):
    bookmarks = Bookmark.objects.filter(user=request.user).select_related('novel', 'chapter')
    return render(request, 'my_bookmarks.html', {'bookmarks': bookmarks})


def bookmark_chapter(request, novel_id, chapter_id):
    novel = get_object_or_404(Novel, id=novel_id)
    chapter = get_object_or_404(Chapter, id=chapter_id, novel=novel)
    Bookmark.objects.get_or_create(user=request.user, novel=novel, chapter=chapter)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def upload_novel(request):
    if request.method == 'POST':
        form = NovelUploadForm(request.POST, request.FILES)

        # Check if there are files in the request
        if 'cover_image' in request.FILES:
            print("Cover image received:", request.FILES['cover_image'])
        else:
            messages.error(request, 'No cover image provided.')
            print("No cover image uploaded.")

        if form.is_valid():
            novel = form.save(commit=False)
            novel.save()
            # Trigger the Celery task
            send_new_novel_notification.delay(novel.id)
            messages.success(request, 'Novel uploaded successfully!')
            return redirect('home')
        else:
            # Display form errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            print(form.errors)
    else:
        form = NovelUploadForm()

    return render(request, 'upload_novel.html', {'form': form})


def add_chapter(request, novel_id):
    novel = get_object_or_404(Novel, pk=novel_id)
    if request.method == 'POST':
        form = ChapterForm(request.POST)
        if form.is_valid():
            chapter = form.save(commit=False)
            chapter.novel = novel
            chapter.save()
            return redirect('novel_detail', novel_id=novel.id)
    else:
        form = ChapterForm()
    return render(request, 'add_chapter.html', {'form': form, 'novel': novel})


def add_review(request, novel_id):
    novel = Novel.objects.get(id=novel_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.novel = novel
            review.user = request.user
            review.save()
            return redirect('novel_detail', novel_id=novel_id)
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form, 'novel': novel})


def search_results(request):
    query = request.GET.get('q')
    novels = Novel.objects.filter(title__icontains=query)
    return render(request, 'search_results.html', {'novels': novels, 'query': query})
