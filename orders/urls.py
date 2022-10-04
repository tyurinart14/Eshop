from orders import views, api_views
from django.urls import path

urlpatterns = [
    path('create/', views.create_new_order,
         name="create_order"),
    path("orders_history", views.orders_user_view,
         name="orders_history"),


    path('api/orders-create-list/', api_views.OrdersListCreateAPIView.as_view(),
         name="orders-create-list"),
    path('api/order-detail-update-delete/<int:pk>/', api_views.OrdersDetailUpdateDeleteAPIView.as_view(),
         name="order-detail-update-delete"),
    path('api/order_item-create-list', api_views.OrderItemsListCreateAPIView.as_view(),
         name="order_item-create-list"),
    path('api/order_item-detail-update-delete/<int:pk>/', api_views.OrderItemDetailUpdateDeleteAPIView.as_view(),
         name="order_item-detail-update-delete")
]
