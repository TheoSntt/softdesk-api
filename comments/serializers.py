from rest_framework import serializers
from comments.models import Comment
from contributors.serializers import UserSerializer
from projects.models import Project

    

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = Comment
        fields = ['id', 'description', 'issue', 'author', 'created_time']


class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'description', 'issue', 'author']
    
    def create(self, validated_data):
        # Get the project and set it as the issue's project
        request = self.context.get('request')
        issue_id = request.parser_context['kwargs']['issue_pk']
        validated_data['issue'] = Project.objects.get(id=issue_id)
        # Get the user id and set it as the issue's author
        user = self.context['request'].user
        validated_data['author'] = user
        # Serializer's create method expected behaviour
        comment = Comment.objects.create(**validated_data)
        return comment

class CommentModifySerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'description']