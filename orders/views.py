from django.shortcuts import render

# Create your views here.
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
class OrderViewSet(viewsets.ViewSet):
    queryset = Order.objects.all()

    def list(self, request):
        serializer = OrderOutSerializer(Order.objects.all(), many=True)
        res = {"success": True, "message": "", "data": serializer.data}
        return Response(res)

    def create(self, request):
        serializer=OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            orderItems= request.data["order_items"]
            order=Order.objects.get(id=serializer.data["id"])
            for orderItem in orderItems:
                product =None
                if(orderItem["product"]!= None):
                    product=Product.objects.get(id=orderItem["product"]["id"])
                
                OrderItem.objects.create(
                    quantity=orderItem["quantity"],
                    price=orderItem["price"],
                    order=order,
                    product=product
                    )
            order.save()

            order = Order.objects.get(id=order.id)
            serializer = OrderOutSerializer(order)
            data={"order":serializer.data}

            res={"success":True,"message":'Data saved.',"data":data}
            return Response(res, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(self.queryset, pk=pk)
        serializer = OrderSerializer(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {"order": serializer.data}
        res = {"success": True, "message": 'Data saved.', "data": data}
        return Response(res)

    def retrieve(self, request, pk=None):
        obj = get_object_or_404(self.queryset, pk=pk)
        serializer = OrderSerializer(obj)
        data = {"order": serializer.data}
        res = {"success": True, "message": 'Data found', "data": data}
        return Response(res)
    


class OrderItemViewSet(viewsets.ViewSet):
    queryset = OrderItem.objects.all()

    def list(self, request):
        serializer = OrderItemSerializer(OrderItem.objects.all(), many=True)
        res = {"success": True, "message": "", "data": serializer.data}
        return Response(res)

    def create(self, request):
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {"success": True, "message": 'Data saved.', "data": serializer.data}
            return Response(res, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(self.queryset, pk=pk)
        serializer = OrderItemSerializer(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {"order_item": serializer.data}
        res = {"success": True, "message": 'Data saved.', "data": data}
        return Response(res)

    def retrieve(self, request, pk=None):
        obj = get_object_or_404(self.queryset, pk=pk)
        serializer = OrderItemSerializer(obj)
        data = {"order_item": serializer.data}
        res = {"success": True, "message": 'Data found', "data": data}
        return Response(res)
    






class StorePlaceViewSet(viewsets.ViewSet):
    queryset = StorePlace.objects.all()

    def list(self, request):
        serializer = StorePlaceSerializer(StorePlace.objects.all(), many=True)
        res = {"success": True, "message": "", "data": serializer.data}
        return Response(res)

    def create(self, request):
        serializer = StorePlaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {"success": True, "message": 'Data saved.', "data": serializer.data}
            return Response(res, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(self.queryset, pk=pk)
        serializer = StorePlaceSerializer(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {"store_place": serializer.data}
        res = {"success": True, "message": 'Data saved.', "data": data}
        return Response(res)

    def retrieve(self, request, pk=None):
        obj = get_object_or_404(self.queryset, pk=pk)
        serializer = StorePlaceSerializer(obj)
        data = {"store_place": serializer.data}
        res = {"success": True, "message": 'Data found', "data": data}
        return Response(res)