from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import OrderItem, Orders
from .serializer import OrdersSerializer, OrderItemSerializer


class OrdersListCreateAPIView(ListCreateAPIView):
    serializer_class = OrdersSerializer
    queryset = Orders.objects.all()


class OrdersDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrdersSerializer
    queryset = Orders.objects.all()


class OrderItemsListCreateAPIView(ListCreateAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()


class OrderItemDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
