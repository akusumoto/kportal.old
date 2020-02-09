"""
Event View
"""

from rest_framework import viewsets, status, permissions
from rest_framework.response import Response

from member.models import User
from .models import Event, EventAnswer, EventUser
from .serializer import EventSerializer, EventAnswerSerializer, EventUserSerializer, EventUserFlattenSerializer

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

    def create(self, request, event_id=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            try:
                event = Event.objects.get(id=event_id)
            except Event.DoesNotExist:
                return Response({"detail":"Event id={} does not exist".format(event_id)}, 
                                status=status.HTTP_400_BAD_REQUEST)
            serializer.save(event=event)
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, event_id=None, pk=None):
        try:
            _event_answer = self.queryset.get(event_id=event_id, pk=pk)
        except:
            return Response({'detail':"Answer id={} does not exist in Event id={}".format(pk, event_id)},
                            status=status.HTTP_400_BAD_REQUEST)
        return super(EventAnswerViewSet, self).retrieve(request, pk=pk)

    def update(self, request, event_id=None, pk=None):
        try:
            event_answer = self.queryset.get(event_id=event_id, pk=pk)
        except:
            return Response({'detail':"Answer id={} does not exist in Event id={}".format(pk, event_id)},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(event_answer, data=request.data)
        if serializer.is_valid():
            serializer.save(event_id=event_id)
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, event_id=None, pk=None):
        try:
            _event_answer = self.queryset.get(event_id=event_id, pk=pk)
        except:
            return Response({'detail':"Answer id={} does not exist in Event id={}".format(pk, event_id)},
                            status=status.HTTP_400_BAD_REQUEST)
        return super(EventAnswerViewSet, self).destroy(request, pk=pk)

class EventUserViewSet(viewsets.ModelViewSet):
    """
    EventUserViewSet
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = EventUser.objects.all()
    serializer_class = EventUserFlattenSerializer

    def list(self, request, event_id=None):
        serializer = self.serializer_class(self.queryset.filter(event_id=event_id), many=True)
        return Response(serializer.data)

    def create(self, request, event_id=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                event = Event.objects.get(id=event_id)
            except Event.DoesNotExist:
                return Response({"detail":"Event id={} does not exist".format(event_id)}, 
                                status=status.HTTP_400_BAD_REQUEST)
            try:
                user = User.objects.get(id=request.data["id"])
            except User.DoesNotExist:
                return Response({"detail":"User id={} does not exist".format(request.data["id"])}, 
                                status=status.HTTP_400_BAD_REQUEST)
            try:
                answer = EventAnswer.objects.get(pk=request.data['answer']['id'])
            except EventAnswer.DoesNotExist:
                errmsg = "Answer '{}' does not exist".format(request.data['answer']['id'])
                return Response({"detail":errmsg},
                                status=status.HTTP_400_BAD_REQUEST)
            except KeyError:
                answer = None
            
            serializer.save(event=event, user=user, answer=answer)
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, event_id=None, user_id=None):
        serializer = self.serializer_class(self.queryset.get(event_id=event_id, user_id=user_id))
        return Response(serializer.data)
    
    def update(self, request, event_id=None, user_id=None):
        """
        update 
        """
        try:
            event_user = EventUser.objects.get(event_id=event_id, user_id=user_id)
        except EventUser.DoesNotExist:
            return Response({"detail":"User id={} does not belong the event".format(user_id)},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer = EventUserFlattenSerializer(event_user, data=request.data)

        if serializer.is_valid():
            try:
                event = Event.objects.get(id=event_id)
            except Event.DoesNotExist:
                return Response({"detail":"Event id={} does not exist".format(event_id)}, 
                                status=status.HTTP_400_BAD_REQUEST)
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                return Response({"detail":"User id={} does not exist".format(user_id)}, 
                                status=status.HTTP_400_BAD_REQUEST)
            try:
                answer = EventAnswer.objects.get(pk=request.data['answer']['id'])
            except EventAnswer.DoesNotExist:
                errmsg = "Answer '{}' does not exist".format(request.data['answer']['id'])
                return Response({"detail":errmsg},
                                status=status.HTTP_400_BAD_REQUEST)
            except KeyError:
                answer = None
                                
            serializer.save(event=event, user=user, answer=answer)
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, event_id=None, user_id=None):
        try:
            event_user = self.queryset.get(event_id=event_id,
                                           user_id=user_id)
            event_user.delete()
            serializer = EventUserFlattenSerializer(event_user)
            return Response(serializer.data)
        except EventUser.DoesNotExist:
            errmsg = "User id={} does not belong to Event id={}".format(user_id, event_id)
            return Response({"detail":errmsg}, status=status.HTTP_400_BAD_REQUEST)

