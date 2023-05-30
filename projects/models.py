from django.db import models
from django.conf import settings


class Project(models.Model):

    class Type(models.TextChoices):
        BACK_END = 'back-end'
        FRONT_END = 'front-end'
        IOS = 'IOS'
        ANDROID = 'Android'
    
    title = models.fields.CharField(max_length=256)
    description = models.fields.CharField(max_length=2048)
    type = models.fields.CharField(choices=Type.choices, max_length=128)

    contributors = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='projects',
        through='contributors.Contributor'
    )
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='projects_authored')
