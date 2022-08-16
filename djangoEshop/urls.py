from djangoEshop import view
from django.urls import path
from django.contrib import admin
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.homepage, name="homepage"),
    path('homepage/', view.homepage),
    path('basket', view.basket, name="basket"),
    path('', include("products.urls")),
    path('', include('user.urls'))
]

handler404 = "djangoEshop.view.handle_not_found"
