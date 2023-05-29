from rest_framework.viewsets import ModelViewSet
from projects.models import Project
from projects.serializers import ProjectDetailSerializer, ProjectListSerializer, ProjectCreateSerializer, ProjectModifySerializer
from rest_framework.permissions import IsAuthenticated
from softdeskapi.permissions import IsAuthorOrReadOnly
from softdeskapi.views import MultipleSerializerMixin, PatchDisallowed



class ProjectViewset(MultipleSerializerMixin, PatchDisallowed, ModelViewSet):
 
    serializer_class = ProjectListSerializer
    detail_serializer_class = ProjectDetailSerializer
    create_serializer_class = ProjectCreateSerializer
    modify_serializer_class = ProjectModifySerializer

    permission_classes = [IsAuthenticated,IsAuthorOrReadOnly]

    # def create(self, request, *args, **kwargs):
    #     request.data['author'] = request.user.id
    #     return super().create(request, *args, **kwargs)
 
    def get_queryset(self):
        user = self.request.user
        projects = Project.objects.filter(contributors__in=[user]) | Project.objects.filter(author=user)
        projects = projects.distinct()
        return projects

    # def partial_update(self, request, *args, **kwargs):
    #     raise MethodNotAllowed('PATCH')
    
    # def _verify_contributors_data(self, contributors, user_id):
    #     if contributors is not None:
    #         if isinstance(contributors, list):
    #             for contributor in contributors:
    #                 if isinstance(contributor, dict):
    #                     if "user" in contributor and "role" in contributor and "permission" in contributor:
    #                         if contributor['user'] == user_id:
    #                             raise ValidationError('The author (request user) must not be passed amongst contributors')
    #                     else:
    #                         raise ValidationError('Missing key in a contributor')
    #                 else:
    #                     raise ValidationError('Within the contributors list, each contributor must be a dict')  
    #         else:
    #             raise ValidationError('Contributors argument is expected to be a list')

    # def _create_contributors(self, contributors, project, user_id):
    #     if contributors is not None:
    #         for ctbt in contributors:
    #             if ctbt['user'] != user_id:
    #                 Contributor.objects.create(user=User.objects.get(id=ctbt['user']),
    #                                            project=project,
    #                                            role=ctbt['role'],
    #                                            permission=ctbt['permission'])
                    
    # def _update_contributors(self, contributors, project, user_id):
    #     if contributors is not None:
    #         # delete contributors
    #         for contributor in project.contributors.all():
    #             contributor.delete()
    #         self._create_contributors(contributors, project, user_id)


    # def perform_create(self, serializer):
    #     # Check wether the contributors data is properly formated
    #     contributors = self.request.data.get('contributors')
    #     self._verify_contributors_data(contributors, self.request.user.id)
    #     # Create the project
    #     instance = serializer.save()
    #     # Set the project's author to the request User
    #     Contributor.objects.create(user=self.request.user,
    #                                              project=instance,
    #                                              role="Auteur",
    #                                              permission="Permission niveau 1")
    #     # Set the project's contributors
    #     self._create_contributors(contributors, instance, self.request.user)
    #     # Calls the normal perform_create function
    #     super().perform_create(serializer)


    # def perform_update(self,serializer):
    #     # Check wether the contributors data is properly formated
    #     contributors = self.request.data.get('contributors')
    #     self._verify_contributors_data(contributors, self.request.user.id)
    #     # Save the project
    #     instance = serializer.save()
    #     # Set the project's contributors
    #     self._update_contributors(contributors, instance, self.request.user)
    #     # Calls the normal perform_update function
    #     super().perform_update(serializer)
