from rest_framework import serializers
from workouts.models import Set
from .exercise_serializer import ExerciseSerializer

class SetSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer(read_only=True)
    workout = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Set
        fields = ['id', 'exercise', 'workout', 'set_number', 'weight', 'reps', 'duration']