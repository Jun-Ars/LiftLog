from django.db import models
from django.contrib.auth import get_user_model
from .workout import Workout

class Exercise(models.Model):
    BARBELL = 'barbell'
    DUMBBELL = 'dumbbell'
    MACHINE = 'machine'
    NO_WEIGHT = 'no_weight'
    DURATION = 'duration'

    EXERCISE_TYPES = [
        (BARBELL, 'Barbell'),
        (DUMBBELL, 'Dumbbell'),
        (MACHINE, 'Machine'),
        (NO_WEIGHT, 'No Weight'),
        (DURATION, 'Duration'),
    ]
    
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=EXERCISE_TYPES)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='exercises')

    def __str__(self):
        return f"{self.name} ({self.workout.name})"
