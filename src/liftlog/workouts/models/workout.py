from django.db import models
from django.contrib.auth import get_user_model

class Workout(models.Model):
    name = models.CharField(max_length=100)
    start = models.DateTimeField()
    end = models.DateTimeField()
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='workouts')

    def __str__(self):
        return f"Workout {self.id}: {self.name}, owned by {self.owner}"