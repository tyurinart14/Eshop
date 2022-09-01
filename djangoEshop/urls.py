from djangoEshop import view
from django.urls import path
from django.contrib import admin
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.HomepageView.as_view(), name="homepage"),
    path('homepage/', view.HomepageView.as_view()),
    path('', include("products.urls")),
    path('', include('user.urls')),
    path('cart/', include('cart.urls')),
    path('', include('orders.urls'))
]

handler404 = "djangoEshop.view.handle_not_found"
