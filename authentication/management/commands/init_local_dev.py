from django.core.management.base import BaseCommand
from authentication.models import User
from projects.models import Project



# ADMIN_PASSWORD = 'password-oc'


class Command(BaseCommand):

    help = 'Initialize project for local development'

    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING(self.help))
        Project.objects.all().delete()
        User.objects.all().delete()

        User.objects.create(email='admin@oc.drf', password='password-oc', first_name="John", last_name="Doe")
        User.objects.create(email='test@oc.drf', password='password-oc', first_name="Bob", last_name="Morane")
        User.objects.create(email='debug@oc.drf', password='password-oc', first_name="Paul", last_name="Bismuth")

        self.stdout.write(self.style.SUCCESS("All Done !"))
