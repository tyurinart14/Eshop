from products import views
from django.urls import path

app_name = "products"

urlpatterns = [
    path('product/<int:num>/', views.product_detail, name="product"),
    path('homepage/<int:number>/', views.CategoryView.as_view(), name="category"),
    path('product/add/', views.CreateNewProduct.as_view(), name="add_product"),
    path('product/change/<pk>/', views.UpdateProductData.as_view(), name="change_product_info")
]
