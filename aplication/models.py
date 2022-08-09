from django.db import models


class ProductContext(models.Model):
    name = models.CharField(max_length=32)
    image = models.TextField(blank=True)
    image2 = models.TextField(blank=True)
    price = models.CharField(max_length=32)
    amount = models.IntegerField(null=True)
    button = models.CharField(max_length=32)
    basket = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32)
    description = models.TextField(blank=True)
    availability = models.BooleanField(null=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)


class Product(models.Model):
    name = models.CharField(max_length=32)
    price = models.CharField(max_length=32)
    amount = models.IntegerField(null=True)
    slug = models.SlugField(max_length=32)
    availability = models.BooleanField(null=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)


class Category(models.Model):
    name = models.CharField(max_length=24)
    slug = models.SlugField(max_length=24)
    description = models.TextField(null=True, blank=True)
