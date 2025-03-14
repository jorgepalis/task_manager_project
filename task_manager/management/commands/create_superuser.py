from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os

class Command(BaseCommand):
    help = 'Crear un superusuario automáticamente durante el despliegue'

    def handle(self, *args, **options):
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
        
        if not password:
            self.stdout.write(self.style.ERROR('No se creó el superusuario: contraseña no configurada'))
            return
            
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS(f'Superusuario {username} creado correctamente'))
        else:
            self.stdout.write(self.style.WARNING(f'El superusuario {username} ya existe'))