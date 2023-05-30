from rest_framework import serializers
from contributors.models import Contributor
from authentication.models import User
from projects.models import Project

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name']
    

class ContributorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Contributor
        fields = ['id', 'user', 'project', 'role', 'permission']


class ContributorCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contributor
        fields = ['id', 'user', 'project', 'role', 'permission']
        read_only_fields = ['project']

    def create(self, validated_data):
        # Get the project and set it as the contributor's project
        request = self.context.get('request')
        project_id = request.parser_context['kwargs']['project_pk']
        validated_data['project'] = Project.objects.get(id=project_id)
        # Serializer's create method expected behaviour
        contributor = Contributor.objects.create(**validated_data)
        return contributor
    
    def validate(self, data):
        request = self.context.get('request')
        project_id = request.parser_context['kwargs']['project_pk']
        project = Project.objects.get(id=project_id)
        if data['user'] == project.author:
            raise serializers.ValidationError("That user is already the project's author. It must not be added to the contributors.")
        return data

class ContributorModifySerializer(serializers.ModelSerializer):

    class Meta:
        model = Contributor
        fields = ['id', 'role', 'permission']