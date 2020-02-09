"""
Serializer
"""
from rest_framework import serializers

from events.serializer import EventSerializer
from .models import Concert

class ConcertSerializer(serializers.ModelSerializer):
    """
    ConcertSerializer
    """

    events = EventSerializer(read_only=True, many=True)
    
    class Meta:
        model = Concert
        fields = '__all__'
        