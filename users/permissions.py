from rest_framework.permissions import BasePermission
from rest_framework import permissions


class IsModerator(BasePermission):
    """Класс проверяет является ли пользователь модератором, проверяя его права"""

    def has_permission(self, request, view):
        return request.user.groups.filter(name="moderators").exists()


class IsOwner(BasePermission):
    """Класс проверяет является ли пользователь владельцем объекта, сравнивая его с авторизованным пользователем"""

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsOwnerOrModeratorWithRestrictions(BasePermission):
    """Класс проверяет доступы, владельцы: полный доступ | модераторы: чтение + редактирование, без создания/удаления"""

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        if view.action == 'create' and IsModerator().has_permission(request, view):
            return False

        return True

    def has_object_permission(self, request, view, obj):

        if IsOwner().has_object_permission(request, view, obj):
            return True

        if IsModerator().has_permission(request, view):
            return view.action in ['retrieve', 'list', 'update', 'partial_update']

        return False