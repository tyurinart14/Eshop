from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from product.models import Product
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def product(request: HttpRequest, item_name: str):
    try:
        item = Product.objects.get(slug=item_name)
        return render(request, 'product_all.html', {'item': item})
    except Product.DoesNotExist:
        raise Http404
