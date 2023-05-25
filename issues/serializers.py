from rest_framework import serializers
from issues.models import Issue
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

class IssueModifySerializer(serializers.ModelSerializer):

    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'tag', 'priority', 'status', 'assignee']