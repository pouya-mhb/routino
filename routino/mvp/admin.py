from django.contrib import admin
from mvp import models
# Register your models here.

admin.site.register(models.Profile)
admin.site.register(models.RoutineGoal)
admin.site.register(models.Routine)
admin.site.register(models.Activity)
