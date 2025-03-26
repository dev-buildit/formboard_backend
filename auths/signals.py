from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth import get_user_model

@receiver(post_migrate)
def create_admin_user(sender, **kwargs):
    """Create a superuser only if it does not exist, after migrations are applied."""
    User = get_user_model()
    if not User.objects.filter(username="admin").exists():
        print("Creating superuser...")
        User.objects.create_superuser("admin", "admin@example.com", "password123")
        print("Superuser created successfully.")
    else:
        print("Superuser already exists. Skipping creation.")
