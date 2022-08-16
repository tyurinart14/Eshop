from products import views
from django.urls import path

urlpatterns = [
    path('product/<str:item_name>/', views.product, name="product"),
    path('homepage/<int:number>/', views.category, name="category"),
]
