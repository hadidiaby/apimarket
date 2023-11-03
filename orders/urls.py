from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
urlpatterns = [
]


router.register(r'orders', views.OrderViewSet, basename='orders')
router.register(r'order-items', views.OrderItemViewSet, basename='order-items')
router.register(r'store-places', views.StorePlaceViewSet, basename='store-places')

urlpatterns=urlpatterns+router.urls