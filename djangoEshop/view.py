from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render
from aplication.models import Product

context_info = [
    {
        "id": "0001",
        "name": "Artur",
        "mail": "example@gmail.com",
        "discount_card": "13722",
        "age": "23",
        "city": "Kharkiv",
        "image": "https://sokol-larkin.com/wp-content/uploads/2021/06/placeholder-image.jpg"
    }
]


def homepage(request: HttpRequest):
    context = {"object": Product.objects.all()}
    return render(request, 'homepage.html', context)


def client_page(request: HttpRequest, id: str):
    for name in context_info:
        if name["id"] == id:
            return render(request, 'client_page.html', name)
    raise Http404


def basket(request: HttpRequest):
    return HttpResponse('Basket')


def product(request: HttpRequest, item_name: str):
    item = Product.objects.all()
    for el in item:
        if el.slug == item_name:
            return render(request, 'product_all.html', {'el': el})
