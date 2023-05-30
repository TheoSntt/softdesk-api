from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from issues.serializers import IssueSerializer, IssueCreateSerializer, IssueModifySerializer
from issues.models import Issue
from softdeskapi.views import MultipleSerializerMixin, PatchDisallowed
from softdeskapi.permissions import IsAuthorOrReadOnly, IsContributorOrNoAcess


class IssueViewset(MultipleSerializerMixin, PatchDisallowed, ModelViewSet):
 
    serializer_class = IssueSerializer
    create_serializer_class = IssueCreateSerializer
    modify_serializer_class = IssueModifySerializer

    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly, IsContributorOrNoAcess]
    
    def get_queryset(self):
        project_id = self.kwargs['project_pk']
        return Issue.objects.filter(project=project_id)

    def create(self, request, *args, **kwargs):
        if "assignee" not in request.data:
            request.data['assignee'] = request.user.id
        return super().create(request, *args, **kwargs)
