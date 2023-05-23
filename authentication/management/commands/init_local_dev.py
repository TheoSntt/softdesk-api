from django.core.management.base import BaseCommand
from authentication.models import User



ADMIN_PASSWORD = 'password-oc'


class Command(BaseCommand):

    help = 'Initialize project for local development'

    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING(self.help))


        User.objects.create_superuser(email='admin@oc.drf', password=ADMIN_PASSWORD)

        self.stdout.write(self.style.SUCCESS("All Done !"))
