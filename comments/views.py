from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from comments.serializers import CommentSerializer, CommentCreateSerializer, CommentModifySerializer
from comments.models import Comment
from softdeskapi.views import MultipleSerializerMixin, PatchDisallowed
from softdeskapi.permissions import IsAuthorOrReadOnly, IsContributorOrNoAcess


class CommentViewset(MultipleSerializerMixin, PatchDisallowed, ModelViewSet):
 
    serializer_class = CommentSerializer
    create_serializer_class = CommentCreateSerializer
    modify_serializer_class = CommentModifySerializer

    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly, IsContributorOrNoAcess]
    
    def get_queryset(self):
        issue_id = self.kwargs['issue_pk']
        return Comment.objects.filter(issue=issue_id)

    # def create(self, request, *args, **kwargs):
    #     issue_id = kwargs.get('issue_pk')
    #     request.data['issue'] = issue_id
    #     request.data['author'] = request.user.id
    #     return super().create(request, *args, **kwargs)
