from django.conf import settings
from django.db import models
from projects.models import Project


class Contributor(models.Model):
    class Permission(models.TextChoices):
        PERM_1 = 'Permission niveau 1'
        PERM_2 = 'Permission niveau 2'
        PERM_3 = 'Permission niveau 3'
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                            #  related_name='contributes'
                             )
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                # related_name='includes'
                                )
    permission = models.fields.CharField(choices=Permission.choices, max_length=128)
    role = models.fields.CharField(max_length=128)

    class Meta:
        unique_together = ('user', 'project',)
