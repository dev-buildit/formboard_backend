from django.apps import AppConfig

class AuthsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auths'

    def ready(self):
        """Import signals on app startup."""
        import auths.signals  # Import the new signal
