"""
urls
"""

from django.urls import path, include
from rest_framework import routers

from .views import ConcertViewSet, ConcertEventViewSet


ROUTER = routers.DefaultRouter()
ROUTER.register('', ConcertViewSet)
#ROUTER.register('<int:event_id>/events/', ConcertEventViewSet)

urlpatterns = [
    path('<int:concert_id>/events/<int:event_id>/', ConcertEventViewSet.as_view({"get":"retrieve", "delete":"destroy"})),
    path('<int:concert_id>/events/', ConcertEventViewSet.as_view({"get":"list", "post":"create"})),
    path('', include(ROUTER.urls)),
]

