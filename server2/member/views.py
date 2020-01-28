"""
views
"""

from django.db import transaction
from django.http.response import JsonResponse, HttpResponse

from rest_framework import viewsets, status, permissions, generics
from rest_framework.response import Response

from .models import User, PART, TYPE, STATUS
from .serializer import UserSerializer, UserDetailSerializer


# ユーザ作成のView(POST)
class AuthRegister(generics.CreateAPIView):
    """
    AuthRegister
    """
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

    @transaction.atomic
    def post(self, request):
        serializer = UserDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ModelViewSet):
    """
    UserViewSet
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class PartViewSet:
    def list(request):
        if request.method == 'GET':
            part_list = []
            for part in PART:
                part_list.append({"id":part[0], "name":part[1]})
            return JsonResponse(part_list, safe=False)

    def detail(request, id):
        if request.method == 'GET':
            part_list = []
            for part in PART:
                if part[0] == id:
                    return JsonResponse({"id":part[0], "name":part[1]})
            else:
                return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

class TypeViewSet:
    def list(request):
        if request.method == 'GET':
            type_list = []
            for type in TYPE:
                type_list.append({"id":type[0], "name":type[1]})
            return JsonResponse(type_list, safe=False)

    def detail(request, id):
        if request.method == 'GET':
            type_list = []
            for type in TYPE:
                if type[0] == id:
                    return JsonResponse({"id":type[0], "name":type[1]})
            else:
                return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

class UserStatusViewSet:
    def list(request):
        if request.method == 'GET':
            status_list = []
            for status in STATUS:
                status_list.append({"id":status[0], "name":status[1]})
            return JsonResponse(status_list, safe=False)

    def detail(request, id):
        if request.method == 'GET':
            status_list = []
            for status in STATUS:
                if status[0] == id:
                    return JsonResponse({"id":status[0], "name":status[1]})
            else:
                return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

