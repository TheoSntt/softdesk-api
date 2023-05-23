from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


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

    objects = UserManager()