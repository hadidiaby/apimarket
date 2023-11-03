
from rest_framework import serializers

from products.serializers import ProductSerializer
from .models import *


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__' 



class OrderItemReadOnlySerializer(serializers.ModelSerializer):
    product= ProductSerializer(many=False,read_only=True)
    class Meta:
        model = OrderItem
        fields = '__all__'


class StorePlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorePlace
        fields = '__all__'



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderOutSerializer(serializers.ModelSerializer):
    order_items = OrderItemReadOnlySerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = '__all__'

