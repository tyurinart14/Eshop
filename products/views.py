from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, UpdateView, CreateView
from django.contrib.auth.mixins import UserPassesTestMixin
import user.models
from products.models import Product
from cart.forms import CartAddProductForm
from user.models import UserModel


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


class CreateNewProduct(UserPassesTestMixin, CreateView):
    model = Product
    fields = ['name', 'image', 'image2', 'price', 'amount', 'slug', 'description', 'availability', 'cat']
    template_name = 'product_add.html'

    def test_func(self):
        return self.request.user.is_staff


class UpdateProductData(UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['name', 'image', 'image2', 'price', 'amount', 'slug', 'description', 'availability', 'cat']
    template_name = 'product_add.html'

    def test_func(self):
        return self.request.user.is_staff
