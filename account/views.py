import json
from django.shortcuts import get_object_or_404
from datetime import date, datetime
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, action
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.models import User

from orders.serializers import OrderOutSerializer

from .models import *
from .serializers import *

# Create your views here.
@api_view(["POST"])
def login_user(request):
    reqBody = json.loads(request.body)
    username = reqBody['phoneNumber']
    password = reqBody['password']
    user=user = authenticate(username=username, password=password)
    if user:
        token, created = Token.objects.get_or_create(user=user)
        token= token.key
        user = CustomUserSerializer(CustomUser.objects.get(user=user)).data
        data = {"token":token,"user":user}
        res={"success":True,"message": "user logged","data":data}
        return Response(res)
    else:
        res={"success":False,"message": "authentification failed","data":{}}
        return Response(res, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(["POST"])
def signup_user(request):
    reqBody = json.loads(request.body)
    try:
        first_name = reqBody['first_name']
        last_name = reqBody['last_name']
        
        username = reqBody['phoneNumber']
        password = reqBody['password']
        phoneNumber = reqBody['phoneNumber']

        if User.objects.filter(username=username).exists():
            data = {}
            res={"success":False,"message": "cet numero a deja été utilisé ","data":data}
            return Response(res, status=status.HTTP_400_BAD_REQUEST) 
        else:
        

            user = User.objects.create(
                username=username,
                last_name=last_name,
                first_name=first_name,
                )
            
            user.set_password(password)
            if 'email' in reqBody:
                user.email = reqBody['email']
            user.save()

            customUser = CustomUser.objects.create(
                user=user,
                phoneNumber=phoneNumber,
            )
            
            token, created = Token.objects.get_or_create(user=user)
            token= token.key
            user = CustomUserSerializer(customUser).data
            data = {"token":token,"user":user}
            res={"success":True,"message": "inscription reussie!","data":data}
            return Response(res)
        
    except Exception as e:
        print(e)
        data = {}
        res={"success":False,"message": "formulaire incorrecte" ,"data":data}
        return Response(res, status=status.HTTP_400_BAD_REQUEST) 






class CustomUserViewSet(viewsets.ViewSet):
    queryset = CustomUser.objects.all()

    def list(self, request):
        serializer = CustomUserSerializer(CustomUser.objects.all(), many=True)
        res = {"success": True, "message": '', "data": serializer.data}
        return Response(res)
    
    @action(detail=True,methods=['get'])
    def orders(self, request,pk=None):
        obj = get_object_or_404(self.queryset, pk=pk)
        serializer = OrderOutSerializer(obj.orders.all(), many=True)
        res = {"success": True, "message": '', "data": serializer.data}
        return Response(res)
    

    def create(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {"success": True, "message": 'Information enregistrée', "data": serializer.data}
            return Response(res, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(self.queryset, pk=pk)
        serializer = CustomUserSerializer(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {"user": serializer.data}
        res = {"success": True, "message": 'Information enregistrée', "data": data}
        return Response(res)

    def retrieve(self, request, pk=None):
        obj = get_object_or_404(self.queryset, pk=pk)
        serializer = CustomUserSerializer(obj)
        data = {"user": serializer.data}
        res = {"success": True, "message": 'Information retrouvée', "data": data}
        return Response(res)
    

    
    def destroy(self, request, pk=None):
        instance = get_object_or_404(self.queryset, pk=pk)
        instance.delete()
        res = {"success": True, "message": 'Data deleted.'}
        return Response(res, status=status.HTTP_204_NO_CONTENT)
    
