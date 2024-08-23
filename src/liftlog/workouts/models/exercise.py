from django.db import models
from django.contrib.auth import get_user_model
from .workout import Workout

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='exercises')

    def __str__(self):
        return f"{self.name} ({self.workout.name})"
