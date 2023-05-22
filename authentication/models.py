from django.contrib.auth.models import AbstractUser
from django.db import models
from projects.models import Project


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = None
    
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

    # projects = models.ManyToManyField(
    #     Project,
    #     symmetrical=True,
    #     # verbose_name='participe à',
    #     related_name='contributors',
    #     through='contributors.Contributor'
    # )


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []