from django.http import HttpRequest, Http404
from django.shortcuts import render
from django.views.generic import DetailView

from products.models import Product


def category(request: HttpRequest, number: str):
    context = {
        'object': Product.objects.filter(cat_id=number)
    }
    return render(request, 'homepage.html', context)


# def product(request: HttpRequest, item_name: str):
#     try:
#         item = Product.objects.get(slug=item_name)
#         return render(request, 'product_all.html', {'item': item})
#     except Product.DoesNotExist:
#         raise Http404

class ProductDetailView(DetailView):
    model = Product
    template_name = "product_all.html"
