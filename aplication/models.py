from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=24)
    slug = models.SlugField(max_length=24)
    description = models.TextField(null=True, blank=True)


class Product(models.Model):
    name = models.CharField(max_length=32)
    image = models.TextField(blank=True)
    image2 = models.TextField(blank=True)
    price = models.IntegerField()
    amount = models.IntegerField(null=True)
    slug = models.SlugField(max_length=32)
    description = models.TextField(blank=True)
    availability = models.BooleanField(null=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
