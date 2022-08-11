from django.contrib import admin
from product.models import Product
from product.models import Category


class ProductAdmin(admin.ModelAdmin):
    list_display = "name", "slug", "cat_id"
    list_display_links = ["name"]
    prepopulated_fields = {
        "slug": ["name"],
    }


class CategoryAdmin(admin.ModelAdmin):
    list_display = "name", "slug", "id"
    list_display_links = ["name"]
    prepopulated_fields = {
        "slug": ["name"],
    }


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)