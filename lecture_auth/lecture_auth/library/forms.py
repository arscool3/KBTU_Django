from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from user.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    # groups = forms.ModelChoiceField(queryset-Group.objects.all())
    class Meta:
        model = CustomUser
        fields = "__all__"


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = "__all__"