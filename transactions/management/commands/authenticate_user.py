from django.core.management.base import BaseCommand
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class Command(BaseCommand):
    help = "Authenticate user and return JWT token"

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username')
        parser.add_argument('password', type=str, help='Password')

    def handle(self, *args, **options):
        username = options['username']
        password = options['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            self.stdout.write(self.style.SUCCESS(f'Token: {access_token}'))
        else:
            self.stdout.write(self.style.ERROR('Invalid credentials'))
