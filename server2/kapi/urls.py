from rest_framework import routers
from .views import UserViewSet, PartViewSet, TypeViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'parts', PartViewSet)
router.register(r'types', TypeViewSet)