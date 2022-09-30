from user.models import UserModel
from .models import OrderItem, Orders
from rest_framework import serializers
from products.models import Product


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"

    def create(self, validated_data):
        OrderItem.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.return_status = validated_data['return_status']

        instance.save()
        return instance


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"

    def create(self, validated_data):
        return Orders.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.order_status = validated_data['order_status']

        instance.save()
        return instance
