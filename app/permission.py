from rest_framework.permissions import BasePermission, SAFE_METHODS

class KursUchunPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return request.method in SAFE_METHODS

class DarsUchunPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.method in SAFE_METHODS:
            return True
        if request.user.is_superuser:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_superuser and request.method == 'DELETE':
            return True
        return False