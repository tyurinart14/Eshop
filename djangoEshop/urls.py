from djangoEshop import view
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.homepage),
    path('homepage/', view.homepage),
    path('client_page/<str:id>', view.client_page),
    path('basket', view.basket),
    path('product/<str:item_name>/', view.product, name="product"),
    path('homepage/<int:number>/', view.category, name="category"),
]

handler404 = "djangoEshop.view.handle_not_found"
