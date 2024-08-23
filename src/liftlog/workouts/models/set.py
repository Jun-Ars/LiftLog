from django.db import models
from django.contrib.auth import get_user_model
from .exercise import Exercise

class Set(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='sets')
    set_number = models.IntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    reps = models.IntegerField()

    def __str__(self):
        return f"Set {self.set_number}: {self.reps} reps at {self.weight} lbs"
