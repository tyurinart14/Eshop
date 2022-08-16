from user import views
from django.urls import path

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('register', views.register_view, name="register"),
    path('client_page/', views.client_page, name="client_page"),
]
