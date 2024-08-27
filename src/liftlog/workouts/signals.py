from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Exercise

User = get_user_model()

@receiver(post_save, sender=User)
def create_default_exercises(sender, instance, created, **kwargs):
    if created:
        # Create these default exercies for every new User
        default_exercises = [
            {"name": "Bench Press", "type": "barbell"},
            {"name": "Squat", "type": "barbell"},
            {"name": "Deadlift", "type": "barbell"},
        ]
        for exercise in default_exercises:
            Exercise.objects.create(
                name=exercise["name"],
                type=exercise["type"],
                user=instance
            )
