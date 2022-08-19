from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from user.models import UserModel


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=15)
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25)
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            UserModel.objects.get(username=username)
            raise ValidationError("A user with this username is already registered")
        except UserModel.DoesNotExist:
            return username

    def clean(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            raise ValidationError("Passwords do not match")

    def create_user(self):
        username = self.cleaned_data["username"]
        first_name = self.cleaned_data["first_name"]
        last_name = self.cleaned_data["last_name"]
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password1"]
        UserModel.objects.create_user(username=username, first_name=first_name,
                                      email=email, last_name=last_name, password=password)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=15, label="Username")
    password = forms.CharField(max_length=25, label="Password", widget=forms.PasswordInput)

    def __int__(self, *args, **kwargs):
        self.user = None
        super().__init__(*args, **kwargs)

    def clean(self):
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]
        self.user = authenticate(username=username, password=password)

        if self.user is None:
            raise ValidationError("Data entered incorrectly")


class ClientPageEditForm(forms.Form):
    first_name = forms.CharField(max_length=15, label="New first_name")
    last_name = forms.CharField(max_length=15, label="New second_name")
    email = forms.EmailField(label="New email")
    username = forms.CharField(max_length=15, label="New username")

    def save(self, user: UserModel):
        UserModel.objects.filter(pk=user.pk).update(**self.cleaned_data)