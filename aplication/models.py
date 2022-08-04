from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=32)
    price = models.CharField(max_length=32)
    amount = models.IntegerField(null=True)
    slug = models.SlugField(max_length=32)
    availability = models.BooleanField(null=True)


class Category(models.Model):
    name = models.CharField(max_length=24)
    slug = models.SlugField(max_length=24)
    description = models.TextField(null=True, blank=True)
