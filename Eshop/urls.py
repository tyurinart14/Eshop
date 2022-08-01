from Eshop import view
from django.urls import path

urlpatterns = [
    path('', view.homepage),
    path('homepage/', view.homepage),
    path('client_page/', view.client_page),
    path('basket', view.basket),
    path('product_1', view.product_1),
    path('product_2', view.product_2),
    path('product_3', view.product_3),
]
