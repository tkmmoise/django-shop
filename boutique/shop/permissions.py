from rest_framework.permissions import BasePermission
from rest_framework.request import HttpRequest

class IsAdminAuthenticated(BasePermission):

    def has_permission(self, request: HttpRequest, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_superuser)