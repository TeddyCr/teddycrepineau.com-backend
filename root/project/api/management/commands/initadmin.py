from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from project.api.models import User

from decouple import config

class Command(BaseCommand):

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            print('Creating username')
            admin = User.objects.create_superuser(
                email=config('DJANGO_EMAIL'),
                password=config('DJANGO_PASSWORD'),
                username=config('DJANGO_USER'))

            admin.is_active = True
            admin.is_admin = True

        