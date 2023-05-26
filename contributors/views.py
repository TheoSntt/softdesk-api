from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from contributors.serializers import ContributorSerializer, ContributorCreateSerializer, ContributorModifySerializer
from contributors.models import Contributor
from softdeskapi.views import MultipleSerializerMixin, PatchDisallowed
from softdeskapi.permissions import IsProjectAuthorOrReadOnly


class UserViewset(MultipleSerializerMixin, PatchDisallowed, ModelViewSet):
 
    serializer_class = ContributorSerializer
    create_serializer_class = ContributorCreateSerializer
    modify_serializer_class = ContributorModifySerializer

    permission_classes = [IsAuthenticated, IsProjectAuthorOrReadOnly]
    queryset = Contributor.objects.all()

    # def create(self, request, *args, **kwargs):
    #     project_id = kwargs.get('project_pk')
    #     request.data['project'] = project_id
    #     return super().create(request, *args, **kwargs)
 

