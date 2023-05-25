from rest_framework import serializers
from projects.models import Project
from contributors.serializers import ContributorSerializer, UserSerializer

class ProjectListSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'author']
    
    # def validate_title(self, value):
    #     if Project.objects.filter(title=value).exists():
    #         raise serializers.ValidationError('Project already exists')
    #     return value
    
    # def validate(self, data):
    #     if data['title'] not in data['description']:
    #         raise serializers.ValidationError('Title must be in description')
    #     return data


class ProjectDetailSerializer(serializers.ModelSerializer):
    contributors = ContributorSerializer(many=True,  source='contributor_set')
    author = UserSerializer()
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'contributors', 'author']
    

class ProjectCreateSerializer(serializers.ModelSerializer):
    # contributors = ContributorSerializer(many=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'contributors', 'author']
        read_only_fields = ['author']
    
    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['author'] = user
        project = Project.objects.create(**validated_data)
        return project
    
    def validate_title(self, value):
        # Nous vérifions que la catégorie existe
        if Project.objects.filter(title=value).exists():
        # En cas d'erreur, DRF nous met à disposition l'exception ValidationError
            raise serializers.ValidationError('Project already exists')
        return value
    

class ProjectModifySerializer(serializers.ModelSerializer):
    # contributors = ContributorSerializer(many=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'contributors']