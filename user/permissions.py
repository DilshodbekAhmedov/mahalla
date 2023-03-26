from rest_framework.permissions import BasePermission

from mahalla.models import Citizen, Neighborhood



class UsersPermissionControl(BasePermission):

    def has_permission(self, request, view):
        from mahalla.views import NeighborhoodViewSet, CitizenViewSet
        if request.user.user_type == "nighborhood_leader":
            if isinstance(view, CitizenViewSet):
                return True
            else:
                return False
        elif request.user.user_type == 'sector_leader':
            if isinstance(view, CitizenViewSet) or \
                    isinstance(view, NeighborhoodViewSet):
                return True
            else:
                return False

        elif request.user.user_type == "measures" or \
                request.user.user_type == "admin" or\
                request.user.is_superuser:
            return True
        else:
            return False




    def has_object_permission(self, request, view, object):

        if request.user.user_type == "nighborhood_leader":
            if isinstance(object, Citizen) and object.neighborhood == request.user.neighborhood:
                return True
            else:
                return False
        elif request.user.user_type == 'sector_leader':
            if isinstance(object, Citizen) and object.neighborhood.sector == request.user.sector:
                return True
            elif isinstance(object, Neighborhood) and object.sector == request.user.sector:
                return True
            else:
                return False

        elif request.user.user_type == "measures" or \
                request.user.user_type == "admin" or \
                request.user.is_superuser:
            return True
        else:
            return False

