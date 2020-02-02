"""
urls
"""

from django.urls import path, include
from rest_framework import routers
from .views import EventViewSet, EventUserViewSet, EventAnswerViewSet


ROUTER = routers.DefaultRouter()
ROUTER.register('users', EventUserViewSet)
ROUTER.register('answers', EventAnswerViewSet)
ROUTER.register('', EventViewSet)

urlpatterns = [
    path('', include(ROUTER.urls)),
]

