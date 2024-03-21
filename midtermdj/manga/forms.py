from django import forms
from .models import UserProfile, Manga, Chapter, Page, Review
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    profile_picture = forms.ImageField(required=False)
    bio = forms.CharField(required=False, widget=forms.Textarea)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'profile_picture', 'bio']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'bio']


class MangaForm(forms.ModelForm):
    class Meta:
        model = Manga
        fields = ['title', 'author', 'summary', 'genre', 'published_date', 'cover_image']
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
        }


class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['title', 'number', 'upload_date']
        widgets = {
            'upload_date': forms.DateInput(attrs={'type': 'date'}),
        }


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['image', 'page_number']


class ReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(choices=[(i, str(i)) for i in range(1, 6)], widget=forms.Select(), label="Rating")

    class Meta:
        model = Review
        fields = ['rating', 'comment']
