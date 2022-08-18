from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth import logout, login
from user.forms import RegisterForm, LoginForm


def client_page(request: HttpRequest):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse_lazy("login"))
    return render(request, 'client_page.html')


def login_view(request: HttpRequest):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            return HttpResponseRedirect(reverse("homepage"))
    else:
        form = LoginForm()
    return render(request, "login_page.html", {"form": form})


def register_view(request: HttpRequest):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.create_user()
            return HttpResponseRedirect(reverse("homepage"))
    else:
        form = RegisterForm()
    return render(request, "register_page.html", {"form": form})


def logout_view(request: HttpRequest):
    logout(request)
    return HttpResponseRedirect(reverse_lazy("homepage"))
