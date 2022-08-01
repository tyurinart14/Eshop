from django.http import HttpRequest
from django.shortcuts import render


def homepage(request: HttpRequest) -> render:
    return render(request, 'homepage.html')


def client_page(request: HttpRequest) -> render:
    return render(request, 'client_file.html')


def basket(request: HttpRequest) -> render:
    return render(request, 'basket.html')


def product_1(request: HttpRequest) -> render:
    return render(request, 'product_1.html')


def product_2(request: HttpRequest) -> render:
    return render(request, 'product_2.html')


def product_3(request: HttpRequest) -> render:
    return render(request, 'product_3.html')
