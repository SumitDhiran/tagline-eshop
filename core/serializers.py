from rest_framework import serializers
from .models import Product,Purchase
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = super(self.__class__, self).create(validated_data)
        return user

    def update(self, instance, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = super().update(instance, validated_data)
        return user


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('owner', 'created_at', 'updated_at',)


class PurchaseSerializer(serializers.ModelSerializer):
    buyer= serializers.ReadOnlyField(source='buyer.username')

    class Meta:
        model = Purchase
        fields = ['id','product','product_name','seller','buyer','purchase_price', 'created_at', 'updated_at',]
        read_only_fields = ('buyer', 'created_at', 'updated_at','seller')
        extra_kwargs = {
            'product': {'write_only': True},
        }