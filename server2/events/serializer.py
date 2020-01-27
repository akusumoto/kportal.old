"""
Serializer
"""
from rest_framework import serializers

from member.serializer import UserSerializer

from .models import Event, EventAnswer, EventUser

class EventSerializer(serializers.ModelSerializer):
    """
    EventSerializer
    """

    owner = UserSerializer(read_only=True)

    class Meta:
        model = Event
        fields = ('id', 'date', 'place', 'subject', 'detail', 'owner')
