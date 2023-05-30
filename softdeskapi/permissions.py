from rest_framework.permissions import BasePermission, SAFE_METHODS
from contributors.models import Contributor
from projects.models import Project

class IsAuthorOrReadOnly(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        # Allow read permissions to any authenticated user
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Allow write permissions only if the user is the author of the project
        return obj.author == request.user

class IsProjectAuthorOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        project_id = view.kwargs['project_pk']
        project = Project.objects.get(id=project_id)
        return project.author == request.user


class IsContributorOrNoAcess(BasePermission):

    def has_permission(self, request, view):
        project_id = view.kwargs['project_pk']
        project = Project.objects.get(id=project_id)
        return Contributor.objects.filter(user=request.user, project=project_id).exists() or project.author == request.user