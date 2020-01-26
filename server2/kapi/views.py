"""
views
"""

from django.db import transaction

from rest_framework import viewsets, status, permissions, generics
from rest_framework.response import Response

from .models import User, Type, Part, UserStatus
from .serializer import UserSerializer, PartSerializer, TypeSerializer, UserStatusSerializer


# ユーザ作成のView(POST)
class AuthRegister(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @transaction.atomic
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserStatusViewSet(viewsets.ModelViewSet):
    """
    UserStatusViewSet
    """
    queryset = UserStatus.objects.all()
    serializer_class = UserStatusSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    UserViewSet
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PartViewSet(viewsets.ModelViewSet):
    """
    PartViewSet
    """
    queryset = Part.objects.all()
    serializer_class = PartSerializer

class TypeViewSet(viewsets.ModelViewSet):
    """
    TypeViewSet
    """
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
