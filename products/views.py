from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import ListView, UpdateView
from products.models import Product
from cart.forms import CartAddProductForm
from products.forms import ProductCreateForm


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


def add_new_product(request):
    if request.method == "POST":
        form = ProductCreateForm(request.POST)
        if form.is_valid():
            form.add_product()
        redirect_url = reverse("homepage")
        return HttpResponseRedirect(redirect_url)
    else:
        form = ProductCreateForm
    return render(request, "product_add.html", {"form": form})


class UpdateProductData(UpdateView):
    model = Product
    fields = ['name', 'image', 'image2', 'price', 'amount', 'slug', 'description', 'availability', 'cat']
    template_name = 'product_add.html'
