"""
serializer
"""

from rest_framework import serializers

from .models import User, Part, Type, UserStatus

class UserStatusSerializer(serializers.ModelSerializer):
    """
    UserStatusSerializer
    """
    class Meta:
        model = UserStatus
        fields = ('id', 'name')

class PartSerializer(serializers.ModelSerializer):
    """
    PartSerializer
    """
    class Meta:
        model = Part
        fields = ('id', 'name')

class TypeSerializer(serializers.ModelSerializer):
    """
    TypeSerializer
    """
    class Meta:
        model = Type
        fields = ('id', 'name')

class UserSerializer(serializers.ModelSerializer):
    """
    UserSerializer
    """
    password = serializers.CharField(write_only=True, required=False)
    part = PartSerializer(read_only=True)
    type = TypeSerializer(read_only=True)
    status = UserStatusSerializer(read_only=True)

    def create(self, validated_data):
        return User.objects.create_user(request_data=validated_data)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'status',
                  'name', 'nickname', 'home_address', 'work_address',
                  'part', 'type', 'emergency_phone', 'note')
        #read_only_fields = ('status', 'part', 'type')

