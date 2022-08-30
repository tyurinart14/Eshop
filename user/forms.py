from django.contrib.auth import forms
from user.models import UserModel


class RegisterForm(forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]


class LoginForm(forms.AuthenticationForm):
    model = UserModel
    fields = ["username", "password"]


class ClientPageEditForm(forms.UserChangeForm):
    class Meta:
        model = UserModel
        fields = ["username", "first_name", "last_name", "email", "password"]
