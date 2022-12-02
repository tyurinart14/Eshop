from rest_framework import serializers
from .models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.image = validated_data['image']
        instance.image2 = validated_data['image2']
        instance.price = validated_data['price']
        instance.amount = validated_data['amount']
        instance.slug = validated_data['slug']
        instance.description = validated_data['description']
        instance.availability = validated_data['availability']
        instance.cat = validated_data['cat']

        instance.save()
        return instance


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
