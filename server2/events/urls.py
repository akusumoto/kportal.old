"""
urls
"""

from django.urls import path, include
from rest_framework import routers
from .views import EventViewSet, EventUserViewSet, EventAnswerViewSet


ROUTER = routers.DefaultRouter()
ROUTER.register('users', EventUserViewSet)
#ROUTER.register('<int:event_id>/answers', EventAnswerViewSet)
ROUTER.register('', EventViewSet)

urlpatterns = [
    path('<int:event_id>/answers/', EventAnswerViewSet.as_view({"get":"list", "post":"create"})),
    path('<int:event_id>/answers/<int:pk>/', EventAnswerViewSet.as_view({"get":"retrieve", "put":"update", "delete":"destroy"})),
    path('<int:event_id>/users/', EventUserViewSet.as_view({"get":"list", "post":"create"})),
    path('<int:event_id>/users/<int:pk>/', EventUserViewSet.as_view({"get":"retrieve", "put":"update", "delete":"destroy"})),
    path('', include(ROUTER.urls)),
]

