from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user


# The default permission policy may be set globally, using the DEFAULT_PERMISSION_CLASSES setting. For example.
#
# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.IsAuthenticated',
#     ]
# }
# If not specified, this setting defaults to allowing unrestricted access:
#
# 'DEFAULT_PERMISSION_CLASSES': [
#    'rest_framework.permissions.AllowAny',
# ]