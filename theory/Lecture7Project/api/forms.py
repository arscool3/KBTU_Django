from django import forms

class PostForm(forms.Form):
    full_name = forms.CharField(label='Full Name', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)


class CommentaryForm(forms.Form):
    text = forms.CharField(label='Comment Text', widget=forms.Textarea)
    user = forms.CharField(label='User', widget=forms.TextInput)
    official_answer = forms.CharField(label='Official Answer', widget=forms.TextInput)
    commentary_type = forms.CharField(label='Commentary Type', widget=forms.TextInput)
    public = forms.BooleanField(label='Public', required=False)