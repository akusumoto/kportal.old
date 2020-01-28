"""
serializer
"""

from rest_framework import serializers

from .models import User

class UserDetailSerializer(serializers.ModelSerializer):
    """
    UserSerializer
    """
    password = serializers.CharField(write_only=True, required=False)

    def create(self, validated_data):
        return User.objects.create_user(request_data=validated_data)
    
    class Meta:
        model = User
        fields = '__all__'
       # ('id', 'username', 'password', 'email', 'status',
       #           'name', 'nickname', 'home_address', 'work_address',
       #           'part', 'type', 'emergency_phone', 'note')
        #read_only_fields = ('status', 'part', 'type')

class UserSerializer(serializers.ModelSerializer):
    """
    SimpleUserSerializer
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'status', 'part', 'nickname')
        read_only_fields = ('id', 'username', 'email', 'status', 'part', 'nickname')
