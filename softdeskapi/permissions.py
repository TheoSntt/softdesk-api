from rest_framework.permissions import BasePermission

class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow read permissions to any authenticated user
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Allow write permissions only if the user is the author of the project
        return obj.author == request.user

class IsProjectAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow read permissions to any authenticated user
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        # Allow write permissions only if the user is the author of the project
        return obj.project.author == request.user