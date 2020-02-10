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

        # for event list - request.data=[{"id":"1"},{"id":"2"}]
        try:
            for obj in request.data:
                event_id = obj['id']
                try:
                    event = Event.objects.get(pk=event_id)
                    concert.events.add(event)
                except: pass
        except: pass

        # for a event - request.data={"id":"1"}
        try:
            event = Event.objects.get(pk=request.data['id'])
            concert.events.add(event)
        except: pass

        serializer = self.serializer_class(concert.events, many=True)
        return Response(serializer.data)

    def retrieve(self, request, concert_id=None, event_id=None):
        concert = Concert.objects.get(id=concert_id)
        try:
            event = concert.events.get(id=event_id)
        except Event.DoesNotExist:
            return Response({"detail":"Event(id={}) does not belong to Concert(id={})".format(event_id, concert_id)},
                     status=status.HTTP_400_BAD_REQUEST)

        serializer = EventSerializer(event)
        return Response(serializer.data)
    
    def destroy(self, request, concert_id=None, event_id=None):
        concert = Concert.objects.get(id=concert_id)
        try:
            event = concert.events.get(id=event_id)
            concert.events.remove(event)
        except Event.DoesNotExist:
            return Response({"detail":"Event(id={}) does not belong to Concert(id={})".format(event_id, concert_id)},
                     status=status.HTTP_400_BAD_REQUEST)
        return Response()

