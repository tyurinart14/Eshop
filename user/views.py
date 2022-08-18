from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from user.forms import RegisterForm


def client_page(request: HttpRequest):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse_lazy("login"))
    return render(request, 'client_page.html')


def login_view(request: HttpRequest):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is None:
            return HttpResponseRedirect(reverse_lazy('login'))
        login(request, user)
        return HttpResponseRedirect(reverse_lazy("homepage"))
    return render(request, "login_page.html")


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
