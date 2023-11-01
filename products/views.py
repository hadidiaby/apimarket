
# Create your views here.

import json

from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from django.db.models import Count
from django.utils import timezone
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from .models import *
from .serializers import *

class CityViewSet(viewsets.ViewSet):
    queryset = City.objects.all()

    def list(self, request):
        serializer = CitySerializer(City.objects.all(), many=True)
        res = {"success": True, "message": "", "data": serializer.data}
        return Response(res)

    def create(self, request):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {"success": True, "message": 'Data saved.', "data": serializer.data}
            return Response(res, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(self.queryset, pk=pk)
        serializer = CitySerializer(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {"city": serializer.data}
        res = {"success": True, "message": 'Data saved.', "data": data}
        return Response(res)

    def retrieve(self, request, pk=None):
        obj = get_object_or_404(self.queryset, pk=pk)
        serializer = CitySerializer(obj)
        data = {"city": serializer.data}
        res = {"success": True, "message": 'Data found', "data": data}
        return Response(res)




class ProductViewSet(viewsets.ViewSet):
    queryset = Product.objects.all()

    def list(self, request):
        serializer = ProductSerializer(Product.objects.all(), many=True)
        res = {"success": True, "message": "", "data": serializer.data}
        return Response(res)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {"success": True, "message": 'Data saved.', "data": serializer.data}
            return Response(res, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(self.queryset, pk=pk)
        serializer = ProductSerializer(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {"product": serializer.data}
        res = {"success": True, "message": 'Data saved.', "data": data}
        return Response(res)

    def retrieve(self, request, pk=None):
        obj = get_object_or_404(self.queryset, pk=pk)
        serializer = ProductSerializer(obj)
        data = {"product": serializer.data}
        res = {"success": True, "message": 'Data found', "data": data}
        return Response(res)