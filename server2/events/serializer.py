"""
Serializer
"""
from rest_framework import serializers

from member.serializer import UserSerializer
from .models import Event, EventAnswer, EventUser


class EventAnswerSerializer(serializers.ModelSerializer):
    """
    EventAnswerSerializer
    """
    #event = EventSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = EventAnswer
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    """
    EventSerializer
    """
    owner = UserSerializer(read_only=True)
    answers = EventAnswerSerializer(many=True)

    """
    def create(self, validated_data):
        answers = validated_data.pop('answers')
        event = Event.objects.create(**validated_data)
        for answer in answers:
            Answer.objects.create(event=event, **answer)
        return event
    """

    class Meta:
        model = Event
        fields = ('id', 'date', 'place', 'subject', 'detail', 'owner', 'answers')


class EventUserSerializer(serializers.ModelSerializer):
    """
    EventUserSerializer
    """
    event = EventSerializer(read_only=True)
    answer = EventAnswerSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = EventUser
        fields = '__all__'
