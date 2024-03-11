from django import forms

from core.models import Article,Comment,Topic,ReadingList

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

class ReadingListForm(forms.ModelForm):
    class Meta:
        model = ReadingList
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'


class EditArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title','short_description','body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'short_description': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        
        }
