from django import forms
from products.models import Product


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'image2', 'price', 'amount', 'slug', 'description', 'availability', 'cat']

    def add_product(self):
        name = self.cleaned_data["name"]
        image = self.cleaned_data["image"]
        image2 = self.cleaned_data["image2"]
        price = self.cleaned_data["price"]
        amount = self.cleaned_data["amount"]
        slug = self.cleaned_data["slug"]
        description = self.cleaned_data["description"]
        availability = self.cleaned_data["availability"]
        cat = self.cleaned_data["cat"]
        Product.objects.create(name=name, image=image, image2=image2, price=price, amount=amount, slug=slug,
                               description=description, availability=availability, cat=cat)
