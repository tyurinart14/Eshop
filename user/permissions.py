from user.models import UserModel
from rest_framework import permissions


class UserProfilePermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: UserModel):
        if request.user.is_superuser:
            return True

        return obj == request.user
