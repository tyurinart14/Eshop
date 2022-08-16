from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from products.models import Product


def homepage(request: HttpRequest):
    context = {"object": Product.objects.all()}
    return render(request, 'homepage.html', context)


def basket(request: HttpRequest):
    return HttpResponse('Basket')


def handle_not_found(request, exception):
    return render(request, 'error_page.html')
