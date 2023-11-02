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
class ProductReadOnlySerializer(serializers.ModelSerializer):
    cityName = serializers.SerializerMethodField('getcityName')
    class Meta:
        model = Product
        fields = '__all__'

    def getcityName(self,product):
        return product.city.name