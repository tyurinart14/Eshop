from orders import views
from django.urls import path


urlpatterns = [
    path('create/', views.create_new_order, name="create_order")
]