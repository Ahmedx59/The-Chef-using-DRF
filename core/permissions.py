from rest_framework.permissions import BasePermission
from users.models import User


class IsSeller(BasePermission):

    def has_permission(self, request, view):     
        return bool(
            request.user and 
            request.user.is_authenticated and
            request.user.user_type == User.UserType.SELLER
        )