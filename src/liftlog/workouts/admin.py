from django.contrib import admin
from .models.exercise import Exercise
from .models.set import Set
from .models.workout import Workout

# Register your models here.
admin.site.register(Exercise)
admin.site.register(Set)
admin.site.register(Workout)