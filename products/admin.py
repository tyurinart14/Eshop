from django.contrib import admin
from products.models import Product
from products.models import Category
from user.models import UserModel


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = "name", "slug", "cat_id"
    list_display_links = ["name"]
    prepopulated_fields = {
        "slug": ["name"],
    }


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "name", "slug", "id"
    list_display_links = ["name"]
    prepopulated_fields = {
        "slug": ["name"],
    }


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = "username", "email", "wallet"
