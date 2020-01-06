from django.urls import path, include
from rest_framework import routers
from .views import UserInfoViewSet, PartViewSet, TypeViewSet, Login

router = routers.DefaultRouter()
router.register(r'userinfos', UserInfoViewSet)
router.register(r'parts', PartViewSet)
router.register(r'types', TypeViewSet)

urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('', include(router.urls)),
]

