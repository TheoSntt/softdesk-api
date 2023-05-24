from rest_framework import serializers
from contributors.models import Contributor
from authentication.models import User

class UserSerializer(serializers.ModelSerializer):

    # user = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name']
    

class ContributorSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Contributor
        fields = ['user', 'role', 'permission']