from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(
        widget=forms.PasswordInput(),
        help_text="Password must contain at least 8 charectors, including alphabets, digits",
        label="Password",
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(),
        help_text="Please enter the same password again",
        label="Confirm Password",
    )

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "password1"]
        help_texts = {
            "username": "Please choose a unique username",
            "password1": "Password must contain at least 8 charectors, including alphabets, digits",
        }
