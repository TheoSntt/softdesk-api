from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from projects.models import Project
from projects.serializers import ProjectDetailSerializer, ProjectListSerializer, ProjectCreateSerializer, ProjectModifySerializer
from rest_framework.permissions import IsAuthenticated
from contributors.models import Contributor
from authentication.models import User
from rest_framework.exceptions import ValidationError


class MultipleSerializerMixin:

    detail_serializer_class = None
    create_serializer_class= None
    modify_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'create' and self.create_serializer_class is not None:
            return self.create_serializer_class
        elif self.action in ['update', 'partial_update'] and self.modify_serializer_class is not None:
            return self.modify_serializer_class
        elif self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class ProjectViewset(MultipleSerializerMixin, ModelViewSet):
 
    serializer_class = ProjectListSerializer
    detail_serializer_class = ProjectDetailSerializer
    create_serializer_class = ProjectCreateSerializer
    modify_serializer_class = ProjectModifySerializer

    permission_classes = [IsAuthenticated]
 
    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(contributors__in=[user])
    
    def perform_create(self, serializer):


        contributors = self.request.data.get('contributors')
        if contributors is not None:
            if isinstance(contributors, list):
                for contributor in contributors:
                    if isinstance(contributor, dict):
                        if "user" in contributor and "role" in contributor and "permission" in contributor:
                            if contributor['user'] == self.request.user.id:
                                raise ValidationError('The author (request user) must not be passed amongst contributors')
                        else:
                            raise ValidationError('Missing key in a contributor')
                    else:
                        raise ValidationError('Within the contributors list, each contributor must be a dict')  
            else:
                raise ValidationError('Contributors argument is expected to be a list')
        
        instance = serializer.save()



        contributor = Contributor.objects.create(user=self.request.user,
                                                 project=instance,
                                                 role="Auteur",
                                                 permission="Permission niveau 1")

        contributors = self.request.data.get('contributors')
        if contributors is not None:
            for ctbt in contributors:
                if ctbt['user'] != self.request.user.id:
                    try:
                        contributor = Contributor.objects.create(user=User.objects.get(id=ctbt['user']),
                                                                project=instance,
                                                                role=ctbt['role'],
                                                                permission=ctbt['permission'])
                    except KeyError:
                        raise ValidationError('Missing key in a contributor')



        
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
