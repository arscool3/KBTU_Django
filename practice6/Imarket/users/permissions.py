from rest_framework import permissions

from users.choices import Role


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_authenticated and request.user and request.user.is_staff


#####################
class IsOwnerOfShop(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.user_type == Role.CUSTOMER:
                return view.action in ['list', 'retrieve']
            else:
                return True

        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.user.user_type == Role.CUSTOMER:
                return view.action in ['retrieve']
            elif request.user.user_type == Role.SELLER:
                return request.user == obj.seller

        return False


#################################

class IsOwnerOfWarehouseItem(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.user_type == Role.CUSTOMER:
                return view.action in ['list', 'retrieve']
            elif request.user.user_type == Role.SELLER:
                return True

        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.user.user_type == Role.CUSTOMER:
                return view.action in ['retrieve']
            elif request.user.user_type == Role.SELLER:
                return request.user == obj.shop.seller

        return False


####################


class IsCustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.user_type == Role.SELLER:
                return view.action in ['list', 'retrieve']

            return True
        return False

    def has_object_permission(self, request, view, obj):
        return bool(request.user.is_authenticated and
                    request.user.user_type == Role.CUSTOMER and
                    request.user == obj.user)
