"""
Event View
"""

from rest_framework import viewsets, status, permissions
from rest_framework.response import Response

from member.models import User
from .models import Event, EventAnswer, EventUser
from .serializer import EventSerializer, EventAnswerSerializer, EventUserSerializer

class EventViewSet(viewsets.ModelViewSet):
    """
    EventViewSet
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def create(self, request):
        """
        create
        """
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            event = serializer.save(owner=request.user)

            if 'answers' in request.data:
                for answer in request.data['answers']:
                    answer_serializer = EventAnswerSerializer(data=answer)
                    if answer_serializer.is_valid():
                        answer_serializer.save(event=event)

            if 'users' in request.data:
                for user in request.data['users']:
                    try:
                        user_obj = User.objects.get(id=user['id'])
                    except User.DoesNotExist:
                        return Response("User(id={}) does not exist".format(user['id']), status=status.HTTP_400_BAD_REQUEST)

                    user_serializer = EventUserSerializer(data=user)
                    if user_serializer.is_valid():
                        user_serializer.save(event=event, user=user_obj)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventAnswerViewSet(viewsets.ModelViewSet):
    """
    EventAnswerViewSet
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = EventAnswer.objects.all()
    serializer_class = EventAnswerSerializer

    def list(self, request, event_id=None):
        serializer = EventAnswerSerializer(self.queryset.filter(event_id=event_id), many=True)
        return Response(serializer.data)

class EventUserViewSet(viewsets.ModelViewSet):
    """
    EventUserViewSet
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = EventUser.objects.all()
    serializer_class = EventUserSerializer

    def list(self, request, event_id=None):
        serializer = self.serializer_class(self.queryset.filter(event_id=event_id), many=True)
        return Response(serializer.data)

