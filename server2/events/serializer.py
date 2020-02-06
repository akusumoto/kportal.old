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

    class Meta:
        model = EventAnswer
        fields = ('id','value')


class EventUserSerializer(serializers.ModelSerializer):
    """
    EventUserSerializer
    """
    #event = EventSerializer(read_only=True)
    answer = EventAnswerSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = EventUser
        fields = ('id', 'user', 'answer', 'comment')

class EventUserFlattenSerializer(serializers.ModelSerializer):
    """
    EventUserFlattenSerializer
    """
    id = serializers.SerializerMethodField(read_only=True)
    #email = serializers.SerializerMethodField(read_only=True)
    nickname = serializers.SerializerMethodField(read_only=True)
    username = serializers.SerializerMethodField(read_only=True)
    answer = serializers.SerializerMethodField()
    
    class Meta:
        model = EventUser
        fields = ('id', 'nickname', 'username', 'answer', 'comment')

    def get_id(self, obj):
        return obj.user.id

    def get_nickname(self, obj):
        return obj.user.nickname

    def get_username(self, obj):
        return obj.user.username

    def get_answer(self, obj):
        if obj.answer:
            return obj.answer.value
        return None

class EventSerializer(serializers.ModelSerializer):
    """
    EventSerializer
    """
    owner = UserSerializer(read_only=True)
    answers = serializers.SerializerMethodField()
    users = serializers.SerializerMethodField()

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
        fields = ('id', 'date', 'place', 'subject', 'detail', 'owner', 'answers', 'users')

    def get_answers(self, obj):
        try:
            answers = EventAnswerSerializer(EventAnswer.objects.filter(event=Event.objects.get(id=obj.id)), many=True).data
            return answers
        except:
            return None

    def get_users(self, obj):
        try:
            users = EventUserFlattenSerializer(EventUser.objects.filter(event=Event.objects.get(id=obj.id)), many=True).data
            return users
        except:
            return None
