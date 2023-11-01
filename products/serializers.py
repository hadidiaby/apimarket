from rest_framework import serializers
from .models import *



class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'