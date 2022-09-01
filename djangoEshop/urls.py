from djangoEshop import view
from django.urls import path
from django.contrib import admin
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.HomepageView.as_view(), name="homepage"),
    path('homepage/', view.HomepageView.as_view()),
    path('basket', view.basket, name="basket"),
    path('', include("products.urls")),
    path('cart/', include('user.urls')),
    path('', include('cart.urls'))
]

handler404 = "djangoEshop.view.handle_not_found"
