from rest_framework import permissions

class UserProfilePermissions(permissions.BasePermission):
    """ Limit the permission of user to edit own profile only if not a admin """


    def has_object_permission(self, request, view, obj):
        """ Check if user is editing his own profile or accessing only get method """
        if request.method in permissions.SAFE_METHODS:
            return True
        return (request.user.id == obj.id or request.user.is_superuser)


class ProfileFeedPermission(permissions.BasePermission):
    """ Limit the permission of user to edit own profile feed only."""


    def has_object_permission(self, request, view, obj):
        """ Check if user is editing his own profile  feed or accessing only get method """
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.id == obj.id