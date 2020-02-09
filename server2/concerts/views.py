from django.shortcuts import render

from rest_framework import viewsets, status, permissions
from rest_framework.response import Response

from events.models import Event
from events.serializer import EventSerializer
from .models import Concert
from .serializer import ConcertSerializer

class ConcertViewSet(viewsets.ModelViewSet):
    """
    ConcertViewSet
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Concert.objects.all()
    serializer_class = ConcertSerializer

class ConcertEventViewSet(viewsets.ModelViewSet):
    """
    ConcertEventViewSet
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def list(self, request, concert_id=None):
        concert = Concert.objects.get(pk=concert_id)
        events = concert.events.all()
        return Response(self.serializer_class(events, many=True).data)

    def create(self, request, concert_id=None):
        concert = Concert.objects.get(pk=concert_id)
        print(concert)
        print(request.data)
        for obj in request.data:
            event_id = obj['id']
            event = Event.objects.get(pk=event_id)
            concert.events.add(event)
        return Response()

    def retrieve(self, request, concert_id=None, event_id=None):
        concert = Concert.objects.get(id=concert_id)
        event = concert.events.get(id=event_id)
        serializer = EventSerializer(event)
        return Response(serializer.data)
    
    def destroy(self, request, concert_id=None, event_id=None):
        pass
