from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from issues.serializers import IssueSerializer, IssueCreateSerializer, IssueModifySerializer
from issues.models import Issue
from softdeskapi.views import MultipleSerializerMixin, PatchDisallowed
from softdeskapi.permissions import IsAuthorOrReadOnly


class IssueViewset(MultipleSerializerMixin, PatchDisallowed, ModelViewSet):
 
    serializer_class = IssueSerializer
    create_serializer_class = IssueCreateSerializer
    modify_serializer_class = IssueModifySerializer

    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    
    def get_queryset(self):
        project_id = self.kwargs['project_pk']
        return Issue.objects.filter(project=project_id)

    # def create(self, request, *args, **kwargs):
    #     project_id = kwargs.get('project_pk')
    #     request.data['project'] = project_id
    #     request.data['author'] = request.user.id
    #     return super().create(request, *args, **kwargs)
