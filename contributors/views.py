from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from contributors.serializers import ContributorSerializer
from contributors.models import Contributor

class UserViewset(ModelViewSet):
 
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated]
    queryset = Contributor.objects.all()

    def create(self, request, *args, **kwargs):
        print("fizz")
        project_id = kwargs.get('project_pk')
        print(project_id)
        request.data['project'] = project_id
        return super().create(request, *args, **kwargs)
 

