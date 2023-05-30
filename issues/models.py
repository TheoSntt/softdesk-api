from django.db import models
from django.conf import settings
from projects.models import Project

class Issue(models.Model):

    class Priorite(models.TextChoices):
        FAIBLE = 'Faible'
        MOYENNE = 'Moyenne'
        ÉLEVÉE = 'Élevée'
    
    class Balise(models.TextChoices):
        BUG = 'Bug'
        AMÉLIORATION = 'Amélioration'
        TÂCHE = 'Tâche'

    class Statut(models.TextChoices):
        A_FAIRE = 'À faire'
        EN_COURS = 'En cours'
        TERMINÉ = 'Terminé'
    
    title = models.fields.CharField(max_length=256)
    description = models.fields.CharField(max_length=2048)
    tag = models.fields.CharField(choices=Balise.choices, max_length=128)
    priority = models.fields.CharField(choices=Priorite.choices, max_length=128)
    status = models.fields.CharField(choices=Statut.choices, max_length=128)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, related_name='issues')
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='issues_authored')
    assignee = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='issues_assigned')
    created_time = models.DateTimeField(auto_now_add=True)