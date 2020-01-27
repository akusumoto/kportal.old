"""
urls
"""

from django.urls import path, include
from rest_framework import routers
from .views import EventViewSet


ROUTER = routers.DefaultRouter()
ROUTER.register('events', EventViewSet)

urlpatterns = [
    path('', include(ROUTER.urls)),
]

