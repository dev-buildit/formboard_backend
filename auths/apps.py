from django.apps import AppConfig
from django.contrib.auth import get_user_model
from django.db.utils import OperationalError, IntegrityError

class AuthsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auths'

    def ready(self):
        """Ensure a superuser is created on deployment if one doesn't exist."""
        from django.core.management import call_command

        try:
            User = get_user_model()
            if not User.objects.filter(username="admin").exists():
                print("Creating superuser...")
                User.objects.create_superuser("admin", "admin@example.com", "password123")
                print("Superuser created successfully.")
            else:
                print("Superuser already exists. Skipping creation.")
        except (OperationalError, IntegrityError):
            print("Database not ready yet. Skipping superuser creation.")
