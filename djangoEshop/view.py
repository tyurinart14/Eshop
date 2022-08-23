from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from products.models import Product


# def homepage(request: HttpRequest):
#     context = {"object": Product.objects.all()}
#     return render(request, 'homepage.html', context)


class HomepageView(ListView):
    model = Product
    template_name = "homepage.html"


def basket(request: HttpRequest):
    return HttpResponse('Basket')


def handle_not_found(request, exception):
    return render(request, 'error_page.html')
