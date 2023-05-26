from rest_framework import generics
from authentication.serializers import UserRegistrationSerializer


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer