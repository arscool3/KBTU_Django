from django import forms
from core.models import Article,Comment,Topic,ReadingList,Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio',)
        widgets = {
            'bio': forms.TextInput(attrs={'class': 'form-control'})
        }


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'short_description', 'topic', 'body']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 10, 'cols': 80}),  # You can adjust the rows and cols as needed
        }
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  
        super(ArticleForm, self).__init__(*args, **kwargs)
        if user:
            self.initial['author'] = user  # Set the initial value for the author field

    def clean_author(self):
        return self.initial['author'] 



class ReadingListForm(forms.ModelForm):
    class Meta:
        model = ReadingList
        fields = ['articles']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

class EditArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title','short_description','body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'short_description': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        
        }
