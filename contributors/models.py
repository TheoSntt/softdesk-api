from django.conf import settings
from django.db import models
from projects.models import Project


class Contributor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                            #  related_name='contributes'
                             )
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                # related_name='includes'
                                )

    class Meta:
        unique_together = ('user', 'project',)
