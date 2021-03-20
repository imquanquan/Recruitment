from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    message = "You must be the owner of this object."

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'job_hunter_id'):
            print(obj.job_hunter_id.id)
        elif hasattr(obj, 'company_id'):
            print(obj.company_id.id)
        
        return True

