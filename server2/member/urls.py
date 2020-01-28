"""
urls
"""

from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, AuthRegister, PartViewSet, TypeViewSet, UserStatusViewSet


ROUTER = routers.DefaultRouter()
ROUTER.register(r'users', UserViewSet)
#ROUTER.register(r'parts', PartViewSet)
#ROUTER.register(r'types', TypeViewSet)

urlpatterns = [
    #path('login', Login.as_view(), name='login'),
    path('register/', AuthRegister.as_view()),
    path('', include(ROUTER.urls)),
    path('parts/', PartViewSet.list, name='parts'),
    path('parts/<id>/', PartViewSet.detail, name='parts'),
    path('types/', TypeViewSet.list, name='types'),
    path('types/<id>/', TypeViewSet.detail, name='types'),
    path('statuses/', UserStatusViewSet.list, name='statuses'),
    path('statuses/<id>/', UserStatusViewSet.detail, name='statuses')
]

