from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from products.models import Product
from cart.forms import CartAddProductForm


class CategoryView(ListView):
    model = Product
    template_name = "homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Product.objects.filter(cat_id=self.kwargs['number'])
        return context


def product_detail(request, num, slug):
    product = get_object_or_404(Product,
                                id=num,
                                slug=slug)
    cart_product_form = CartAddProductForm()
    return render(request, 'product_detail.html', {'product': product,
                                                   'cart_product_form': cart_product_form})
