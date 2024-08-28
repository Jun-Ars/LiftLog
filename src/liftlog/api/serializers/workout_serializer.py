from rest_framework import serializers
from workouts.models import Workout
from .set_serializer import SetSerializer

class WorkoutSerializer(serializers.ModelSerializer):
    workout_sets = SetSerializer(many=True, read_only=True)

    class Meta:
        model = Workout
        fields = ['id', 'name', 'start', 'end', 'owner', 'workout_sets']