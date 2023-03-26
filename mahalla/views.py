from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from user.permissions import UsersPermissionControl
from .models import Sector, Neighborhood, Citizen
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import SectorSerializer, NeighborhoodSerializer, CitizenSerializer

class SectorViewSet(ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, UsersPermissionControl]
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer

class NeighborhoodViewSet(ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, UsersPermissionControl]
    queryset = Neighborhood.objects.all()
    serializer_class = NeighborhoodSerializer

class CitizenViewSet(ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, UsersPermissionControl]
    queryset = Citizen.objects.all()
    serializer_class = CitizenSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.user_type == 'nighborhood_leader':
            qs = qs.filter(neighborhood=self.request.user.neighborhood)
        return qs
