from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
urlpatterns = [
    
]


router.register(r'cities', views.CityViewSet, basename='cities')
router.register(r'products', views.ProductViewSet, basename='products')

urlpatterns=urlpatterns+router.urls