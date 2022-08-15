from djangoEshop import view
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.homepage, name="homepage"),
    path('homepage/', view.homepage),
    path('client_page/', view.client_page,  name="client_page"),
    path('basket', view.basket, name="basket"),
    path('product/<str:item_name>/', view.product, name="product"),
    path('homepage/<int:number>/', view.category, name="category"),
    path('login/', view.login_view, name="login"),
    path('logout', view.logout_view, name="logout"),
    path('register', view.register_view, name="register"),
]

handler404 = "djangoEshop.view.handle_not_found"
