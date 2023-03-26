from django.urls import path, include

from user.views import UserViewSet
from .views import SectorViewSet, NeighborhoodViewSet, CitizenViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('sectors', SectorViewSet)
router.register('neibars', NeighborhoodViewSet)
router.register('citizens', CitizenViewSet)
router.register('user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
