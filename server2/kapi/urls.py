"""
urls
"""

from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, PartViewSet, TypeViewSet, Login

ROUTER = routers.DefaultRouter()
ROUTER.register(r'users', UserViewSet)
ROUTER.register(r'parts', PartViewSet)
ROUTER.register(r'types', TypeViewSet)

urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('', include(ROUTER.urls)),
]
