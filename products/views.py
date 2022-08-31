from django.views.generic import DetailView, ListView
from products.models import Product


class CategoryView(ListView):
    model = Product
    template_name = "homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Product.objects.filter(cat_id=self.kwargs['number'])
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
