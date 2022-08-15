from django.urls import path
from product import views


urlpatterns = [
    path('product/<str:item_name>/', views.product, name="product")
]