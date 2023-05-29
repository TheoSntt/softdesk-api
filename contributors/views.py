from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from contributors.serializers import ContributorSerializer, ContributorCreateSerializer, ContributorModifySerializer
from contributors.models import Contributor
from softdeskapi.views import MultipleSerializerMixin, PatchDisallowed
from softdeskapi.permissions import IsAuthorOrReadOnly
from django.db import IntegrityError
from rest_framework.response import Response


class UserViewset(MultipleSerializerMixin, PatchDisallowed, ModelViewSet):
 
    serializer_class = ContributorSerializer
    create_serializer_class = ContributorCreateSerializer
    modify_serializer_class = ContributorModifySerializer

    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            return Response({'message': 'User already listed in this project\'s contributors'}, status=400)
    
    def get_queryset(self):
        project_id = self.kwargs['project_pk']
        return Contributor.objects.filter(project=project_id)
 

