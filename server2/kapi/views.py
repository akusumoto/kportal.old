"""
views
"""

import json

from django.http.response import JsonResponse
from rest_framework import viewsets, views

from .models import User, Type, Part, UserStatus, AccessToken
from .serializer import UserSerializer, PartSerializer, TypeSerializer, UserStatusSerializer

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

class Login(views.APIView):
    """
    Login
    """

    def post(self, request):
        """
        POST method
        """
        try:
            data = json.loads(request.body)
            username = data['username']
            password = data['password']
        except:
            return JsonResponse({'message':'invalid JSON'}, status=400)

        if not User.objects.filter(username=username).exists():
            return JsonResponse({'message':'login failure'}, status=403)

        user = User.objects.get(username=username)

        if not user.check_password(password):
            return JsonResponse({'message':'login failure'}, status=403)

        token = AccessToken.create(user)

        return JsonResponse({'token': token.token})
