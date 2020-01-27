"""
Event View
"""

from django.shortcuts import render
from rest_framework import viewsets, status, permissions, generics
from rest_framework.response import Response

from .models import Event, EventAnswer, EventUser
from .serializer import EventSerializer

class EventViewSet(viewsets.ModelViewSet):
    """
    EventViewSet
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Event.objects.all()
    serializer_class = EventSerializer