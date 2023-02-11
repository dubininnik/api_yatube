# Это решение было подсмотрено у коллег, которые уже прошли ревью,
# и погуглить примеры кастомных разрешений.
from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsOwnerOrAuthReadOnly(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (
            request.method in SAFE_METHODS
            or obj.author == request.user
        )
