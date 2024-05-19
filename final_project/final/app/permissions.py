from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthenticatedForGETRequests(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user and request.user.is_authenticated
        return True


class IsAdminForOtherRequests(BasePermission):

    def has_permission(self, request, view):
        if request.method in ['POST', 'PUT', 'DELETE']:
            return request.user and request.user.is_staff
        return True
