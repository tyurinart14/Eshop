from djangoEshop import view
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.homepage, name="homepage"),
    path('homepage/', view.homepage),
    path('basket', view.basket, name="basket"),
    path('homepage/<int:number>/', view.category, name="category"),
    path('', include('product.urls')),
    path('', include('user.urls'))
]

handler404 = "djangoEshop.view.handle_not_found"
