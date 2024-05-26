# links_app/permissions.py
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission to only allow admins to edit or delete objects.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class IsAdminUser(BasePermission):
    """
    Custom permission to only allow admins to add objects.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_staff
