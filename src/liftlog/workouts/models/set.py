from django.db import models
from django.contrib.auth import get_user_model
from .exercise import Exercise

class Set(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='sets')
    set_number = models.IntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True) # Weight is optional for non-weighted exercises
    reps = models.IntegerField(null=True, blank=True)  # Reps are optional for duration-based exercises
    duration = models.DurationField(null=True, blank=True)  # Duration is optional for rep-based exercises


    def __str__(self):
        if self.exercise.type == Exercise.DURATION:
            return f"{self.exercise} set {self.set_number}: {self.duration} seconds"
        else:
            return f"{self.exercise} set {self.set_number}: {self.reps} reps at {self.weight} lbs"
