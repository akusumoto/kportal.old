from django.shortcuts import render
from django.http.response import JsonResponse
from django.contrib.auth.models import User
import django_filters

from rest_framework import viewsets, filters, views

from .models import UserInfo, Type, Part, UserStatus, AccessToken
from .serializer import UserInfoSerializer, PartSerializer, TypeSerializer, UserStatusSerializer

import json

class UserStatusViewSet(viewsets.ModelViewSet):
    queryset = UserStatus.objects.all()
    serializer_class = UserStatusSerializer

class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

class PartViewSet(viewsets.ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class Login(views.APIView):
    def post(self, request, format=None):
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


