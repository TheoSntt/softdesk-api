from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from projects.models import Project
from projects.serializers import ProjectDetailSerializer, ProjectListSerializer, ProjectCreateSerializer
from rest_framework.permissions import IsAuthenticated
from contributors.models import Contributor


class MultipleSerializerMixin:

    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'create' and self.create_serializer_class is not None:
            return self.create_serializer_class
        elif self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class ProjectViewset(MultipleSerializerMixin, ModelViewSet):
 
    serializer_class = ProjectListSerializer
    detail_serializer_class = ProjectDetailSerializer
    create_serializer_class = ProjectCreateSerializer

    permission_classes = [IsAuthenticated]
 
    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(contributors__in=[user])
    
    def perform_create(self, serializer):
        # project = serializer.save()
        # print(self.request.data)
        # print(serializer)
        req_user = self.request.user

        # print(self.request.data['contributors'])

        instance = serializer.save()

        contributor = Contributor.objects.create(user=req_user,
                                                 project=instance,
                                                 role="Auteur",
                                                 permission="Permission niveau 1")

        super().perform_create(serializer)

        # title_data = self.request.data.get('title')
        # description_data = self.request.data.get('description')
        # type_data = self.request.data.get('type')
        # author_data = self.request.data.get('author')
        # contributors_data = self.request.data.get('contributors')

        # instance = Project.objects.create(title=title_data,
        #                                   description=description_data,
        #                                   type=type_data,
        #                                   author=author_data)
        # instance.contributors.add(*users)


        # contributors_data = self.request.data.pop('contributors', [])
        # project = serializer.save()
        # for contributor_data in contributors_data:
        #     contributor_data['project'] = project.id
        #     Contributor.objects.create(**contributor_data)
