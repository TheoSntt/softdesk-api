from rest_framework import serializers
from projects.models import Project

class ProjectListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'contributors', 'autor']
    
    # def validate_title(self, value):
    #     if Project.objects.filter(title=value).exists():
    #         raise serializers.ValidationError('Project already exists')
    #     return value
    
    # def validate(self, data):
    #     if data['title'] not in data['description']:
    #         raise serializers.ValidationError('Title must be in description')
    #     return data


class ProjectDetailSerializer(serializers.ModelSerializer):

    contributors = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'contributors', 'autor']

    # def get_contributors(self, instance):
    #     queryset = instance.contributors.all()
    #     serializer = ContributorListSerializer(queryset, many=True)
    #     return serializer.data