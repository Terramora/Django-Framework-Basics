from django.contrib.auth.forms import User
from users.models import User
from users.forms import UserRegistrationForm, UserProfileForm
from django import forms


class UserAdminRegistratinonForm(UserRegistrationForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'custom-file-input'
    }), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

class UserAdminProfileForm(UserProfileForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4'
    }))