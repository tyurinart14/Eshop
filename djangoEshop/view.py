from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from product.models import Product


def category(request: HttpRequest, number: str):
    context = {
        'object': Product.objects.filter(cat_id=number)
    }
    return render(request, 'homepage.html', context)


def homepage(request: HttpRequest):
    context = {"object": Product.objects.all()}
    return render(request, 'homepage.html', context)


def basket(request: HttpRequest):
    return HttpResponse('Basket')


def handle_not_found(request, exception):
    return render(request, 'error_page.html')
