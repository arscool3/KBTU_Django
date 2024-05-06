from rest_framework.permissions import BasePermission

class IsCustomUserAuthenticated(BasePermission):
    def has_permission(self, request, view):
        profile_id = request.query_params.get('profile_id')
        if profile_id is None:
            return False
        return True
