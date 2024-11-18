from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import AppUser


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60)
    username = forms.CharField(max_length=50)

    class Meta:
        model = AppUser
        fields = ["username", "email", "password1", "password2"]
