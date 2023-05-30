from rest_framework import serializers
from issues.models import Issue
from projects.models import Project
from authentication.models import User
from contributors.serializers import UserSerializer

    

class IssueSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    assignee = UserSerializer()
    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'tag', 'priority', 'status', 'project', 'author', 'assignee']


class IssueCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'tag', 'priority', 'status', 'project', 'author', 'assignee']
        read_only_fields = ['project', 'author']
    
    def create(self, validated_data):
        # Get the project and set it as the issue's project
        request = self.context.get('request')
        project_id = request.parser_context['kwargs']['project_pk']
        validated_data['project'] = Project.objects.get(id=project_id)
        # Get the user id and set it as the issue's author
        user = self.context['request'].user
        validated_data['author'] = user
        # Serializer's create method expected behaviour
        issue = Issue.objects.create(**validated_data)
        return issue

    def validate_assignee(self, value):
        print(value)
        if value:
            # Retrieve the assigned user
            user = value
            # Retrieve the Project
            request = self.context.get('request')
            project_id = request.parser_context['kwargs']['project_pk']
            project = Project.objects.get(id=project_id)
            # Checks whether the User is a contributor (or author) to the project
            if project not in user.projects.all() and user != project.author:
                raise serializers.ValidationError('That user do not contribute to that project.')
        return value

class IssueModifySerializer(serializers.ModelSerializer):

    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'tag', 'priority', 'status', 'assignee']