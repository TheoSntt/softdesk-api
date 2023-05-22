from django.db import models
from django.conf import settings
from issues.models import Issue

class Comment(models.Model):
    description = models.fields.CharField(max_length=1024)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    issue = models.ForeignKey(to=Issue, on_delete=models.CASCADE, related_name='comments')
    created_time = models.DateTimeField(auto_now_add=True)