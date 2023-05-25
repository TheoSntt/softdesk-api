from rest_framework import serializers
from comments.models import Comment
from contributors.serializers import UserSerializer

    

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = Comment
        fields = ['id', 'description', 'issue', 'author', 'created_time']


class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'description', 'issue', 'author']

class CommentModifySerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'description']