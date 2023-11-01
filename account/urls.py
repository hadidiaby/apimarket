from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
urlpatterns = [
    path('login/',views.login_user, name='login'),
    path('signup/',views.signup_user, name='signup'),
]


router.register(r'users', views.CustomUserViewSet, basename='users')

urlpatterns=urlpatterns+router.urls