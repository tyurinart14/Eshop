from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import OrderItem, Orders
from .serializer import OrdersSerializer, OrderItemSerializer
from rest_framework import permissions


class OrdersListCreateAPIView(ListCreateAPIView):
    serializer_class = OrdersSerializer
    queryset = Orders.objects.all()
    permission_classes = [permissions.IsAdminUser]


class OrdersDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrdersSerializer
    queryset = Orders.objects.all()
    permission_classes = [permissions.IsAdminUser]


class OrderItemsListCreateAPIView(ListCreateAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
    permission_classes = [permissions.IsAdminUser]


class OrderItemDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
    permission_classes = [permissions.IsAdminUser]
