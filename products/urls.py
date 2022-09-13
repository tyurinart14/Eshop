from products import views
from django.urls import path

urlpatterns = [
    path('product/<int:num>/<slug:slug>/', views.product_detail, name="product"),
    path('homepage/<int:number>/', views.CategoryView.as_view(), name="category"),
    path('product/add/', views.CreateNewProduct.as_view(), name="add_product"),
    path('product/change/<slug:slug>/', views.UpdateProductData.as_view(), name="change_product_info")
]
