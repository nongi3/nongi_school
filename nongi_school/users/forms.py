from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    # email = forms.EmailField()

    class Meta:
        model = User

        fields = ['first_name', 'last_name']
        labels = {
            "first_name": "Имя",
            "last_name": "Фамилия"
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = ['image']
        exclude = ['karma', 'confirmed']
        labels = {
            "image": "Аватар"
        }

    def unconfirmed(self):
        self.Meta.model.confirmed = False


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = ['image', 'karma', 'confirmed']
        labels = {
            "image": "Аватар",
            'karma': 'карма',
            'confirmed': "подтвержден"
        }
