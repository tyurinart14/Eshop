from products import views
from django.urls import path

urlpatterns = [
    path('product/<int:num>/<slug:slug>/', views.product_detail, name="product"),
    path('homepage/<int:number>/', views.CategoryView.as_view(), name="category"),
]
