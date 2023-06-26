from rest_framework import permissions

class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True  # Permitir operaciones de lectura para todos los usuarios

        return request.user.is_authenticated  # Permitir operaciones de escritura solo para usuarios autenticados
