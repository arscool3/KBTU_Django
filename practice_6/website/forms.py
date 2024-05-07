from django import forms
from .models import Novel, Chapter, Review
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture']


class NovelUploadForm(forms.ModelForm):
    class Meta:
        model = Novel
        fields = ['title', 'author', 'summary', 'cover_image']
        widgets = {
            'summary': forms.Textarea(attrs={'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cover_image'].widget.attrs['accept'] = 'image/*'


class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['title', 'content', 'chapter_number']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Chapter title'}),
            'content': forms.Textarea(attrs={'placeholder': 'Chapter content'}),
            'chapter_number': forms.NumberInput(attrs={'min': 1}),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']

class SearchForm(forms.Form):
    q = forms.CharField(label='Search', max_length=100)