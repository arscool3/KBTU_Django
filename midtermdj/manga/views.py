from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404, redirect
from .models import Manga, Chapter, Page, UserProfile
from django.contrib.auth.models import User
from .forms import UserProfileForm, MangaForm, ChapterForm, PageForm, ReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.save()
            user.refresh_from_db()
            profile = user.profile
            profile.bio = form.cleaned_data.get('bio')
            if 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']
            profile.save()

            messages.success(request, 'Your account has been created! You are now able to log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def manga_list(request):
    mangas = Manga.objects.all()
    return render(request, 'manga_list.html', {'mangas': mangas})


def manga_detail(request, manga_id):
    manga = get_object_or_404(Manga, id=manga_id)
    reviews = manga.reviews.all()

    if request.method == 'POST' and request.user.is_authenticated:
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.user = request.user
            new_review.manga = manga
            new_review.save()
            return redirect('manga_detail', manga_id=manga.id)
    else:
        review_form = ReviewForm()

    return render(request, 'manga_detail.html', {
        'manga': manga,
        'reviews': reviews,
        'review_form': review_form
    })


def chapter_detail(request, chapter_id):
    chapter = get_object_or_404(Chapter, id=chapter_id)
    pages = chapter.pages.all()
    manga = chapter.manga
    chapters = manga.chapters.all().order_by('number')

    # Find previous and next chapter
    previous_chapter = None
    next_chapter = None
    for index, current in enumerate(chapters):
        if current == chapter:
            if index > 0:
                previous_chapter = chapters[index - 1]
            if index < len(chapters) - 1:
                next_chapter = chapters[index + 1]
            break

    return render(request, 'chapter_detail.html', {
        'chapter': chapter,
        'pages': pages,
        'previous_chapter': previous_chapter,
        'next_chapter': next_chapter
    })


def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    bio = user.profile.bio
    profile_picture_url = user.profile.profile_picture.url
    return render(request, 'user_profile.html', {
        'user': user,
        'bio': bio,
        'profile_picture_url': profile_picture_url
    })


def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'user_profile.html', {'user_profile': user_profile})


def edit_user_profile(request, username):
    user = get_object_or_404(User, username=username)

    if request.user != user:
        messages.error(request, "You do not have permission to edit this profile.")
        return redirect('user_profile', username=username)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully!")
            return redirect('user_profile', username=username)
    else:
        form = UserProfileForm(instance=user.profile)

    return render(request, 'edit_user_profile.html', {'form': form, 'profile_user': user})


def upload_manga(request):
    if request.method == 'POST':
        form = MangaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manga_list')
    else:
        form = MangaForm()
    return render(request, 'manga_upload.html', {'form': form})


def add_chapter(request, manga_id):
    manga = get_object_or_404(Manga, id=manga_id)
    if request.method == 'POST':
        form = ChapterForm(request.POST)
        if form.is_valid():
            new_chapter = form.save(commit=False)
            new_chapter.manga = manga
            new_chapter.save()
            return redirect('upload_page', chapter_id=new_chapter.id)
    else:
        form = ChapterForm()
    return render(request, 'add_chapter.html', {'form': form, 'manga': manga})


def upload_page(request, chapter_id):
    chapter = get_object_or_404(Chapter, id=chapter_id)
    if request.method == 'POST':
        images = request.FILES.getlist('images')
        page_numbers = request.POST.getlist('page_number')

        for img, num in zip(images, page_numbers):
            Page.objects.create(chapter=chapter, image=img, page_number=num)

        return redirect('chapter_detail', chapter_id=chapter.id)

    return render(request, 'upload_page.html', {'chapter': chapter})


def logout_view(request):
    logout(request)
    return redirect('manga_list')
