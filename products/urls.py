from products import views
from django.urls import path

urlpatterns = [
    path('product/<slug:slug>/', views.ProductDetailView.as_view(), name="product"),
    path('homepage/<int:number>/', views.category, name="category"),
]
