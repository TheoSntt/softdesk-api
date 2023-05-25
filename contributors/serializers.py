from rest_framework import serializers
from contributors.models import Contributor
from authentication.models import User

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

class ContributorModifySerializer(serializers.ModelSerializer):

    class Meta:
        model = Contributor
        fields = ['id', 'role', 'permission']