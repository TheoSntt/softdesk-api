from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from projects.models import Project
from projects.serializers import ProjectDetailSerializer, ProjectListSerializer

class MultipleSerializerMixin:

    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class ProjectViewset(MultipleSerializerMixin, ModelViewSet):
 
    serializer_class = ProjectListSerializer
    detail_serializer_class = ProjectDetailSerializer
 
    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(contributors__in=[user])


# class ProjectViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):

#     serializer_class = ProjectListSerializer
#     detail_serializer_class = ProjectDetailSerializer

#     def get_queryset(self):
#         # return Project.objects.filter(active=True)
#         return Project.objects.all()