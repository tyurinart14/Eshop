from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=24)
    slug = models.SlugField(max_length=24)
    description = models.TextField(null=True, blank=True)


class Product(models.Model):
    name = models.CharField(max_length=32)
    image = models.TextField()
    image2 = models.TextField()
    price = models.IntegerField()
    amount = models.IntegerField(null=True, default=0)
    slug = models.SlugField(max_length=32)
    description = models.TextField()
    availability = models.BooleanField(null=True, default=False)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    class Meta:
        db_table = "products_product"
        verbose_name = "product"

    def get_absolute_url(self):
        return reverse("homepage")
