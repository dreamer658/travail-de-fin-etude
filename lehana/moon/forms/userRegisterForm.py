from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    """UserSignupForm custom made class"""

    class Meta:
        """Meta definition of UserSignupForm"""
        email = forms.EmailField()
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]
