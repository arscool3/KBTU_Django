from rest_framework import permissions

class IsManagerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only managers to edit objects.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated and hasattr(request.user, 'manager')

class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and hasattr(request.user, 'manager')

class IsAdminUserOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only admin users to edit objects.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated and request.user.is_staff

class IsBookingClient(permissions.BasePermission):
    """
    Custom permission to allow only booking clients to edit their own bookings.
    """
    def has_object_permission(self, request, obj, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated and obj.client == request.user

class IsManagerCanChangeStatus(permissions.BasePermission):
    """
    Custom permission to allow only managers to change the status of booking requests or application requests.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated and hasattr(request.user, 'manager')