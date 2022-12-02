from .models import UserModel
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username', 'password', 'first_name', 'last_name', 'email', 'is_superuser', 'is_staff', 'wallet')

    def create(self, validated_data):
        return UserModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data['username']
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.email = validated_data['email']
        instance.wallet = validated_data['wallet']
        instance.password = validated_data['password']

        instance.save()
        return instance
