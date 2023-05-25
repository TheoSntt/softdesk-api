from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from issues.serializers import IssueSerializer, IssueCreateSerializer, IssueModifySerializer
from issues.models import Issue
from softdeskapi.views import MultipleSerializerMixin

class IssueViewset(MultipleSerializerMixin, ModelViewSet):
 
    serializer_class = IssueSerializer
    create_serializer_class = IssueCreateSerializer
    modify_serializer_class = IssueModifySerializer

    permission_classes = [IsAuthenticated]
    queryset = Issue.objects.all()

    def create(self, request, *args, **kwargs):
        project_id = kwargs.get('project_pk')
        request.data['project'] = project_id
        request.data['author'] = request.user.id
        return super().create(request, *args, **kwargs)
