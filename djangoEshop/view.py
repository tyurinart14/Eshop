from django.http import HttpRequest, HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from aplication.models import Product
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def category(request: HttpRequest, number: str):
    context = {
        'object': Product.objects.filter(cat_id=number)
    }
    return render(request, 'homepage.html', context)


def homepage(request: HttpRequest):
    context = {"object": Product.objects.all()}
    return render(request, 'homepage.html', context)


def client_page(request: HttpRequest):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse_lazy("login"))
    return render(request, 'user_templates/client_page.html')


def basket(request: HttpRequest):
    return HttpResponse('Basket')


def product(request: HttpRequest, item_name: str):
    try:
        item = Product.objects.get(slug=item_name)
        return render(request, 'product_all.html', {'item': item})
    except Product.DoesNotExist:
        raise Http404


def handle_not_found(request, exception):
    return render(request, 'error_page.html')


def login_view(request: HttpRequest):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is None:
            return HttpResponseRedirect(reverse_lazy('login'))
        login(request, user)
        return HttpResponseRedirect(reverse_lazy("homepage"))
    return render(request, "user_templates/login_page.html")


def register_view(request: HttpRequest):
    if request.method == "POST":
        username = request.POST["username"]
        if User.objects.filter(username=username):
            context = {"message": "User exists"}
            return render(request, "user_templates/register_page.html", context)

        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        email = request.POST["email"]
        first_name = request.POST["first_name"]
        last_name = request.POST["second_name"]

        if password1 == password2:
            User.objects.create_user(username=username, password=password2,
                                     email=email, first_name=first_name, last_name=last_name)
            return HttpResponseRedirect(reverse_lazy("login"))

    return render(request, "user_templates/register_page.html")


def logout_view(request: HttpRequest):
    logout(request)
    return HttpResponseRedirect(reverse_lazy("homepage"))
