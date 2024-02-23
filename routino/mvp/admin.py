from django.contrib import admin
from mvp import models
# Register your models here.

# admin.site.register(models.Profile)
# admin.site.register(models.RoutineGoal)
# admin.site.register(models.Routine)
# admin.site.register(models.Activity)
# admin.site.register(models.ActivityType)


@admin.register(models.ActivityType)
class ActivityTypeAdmin (admin.ModelAdmin):
    list_display = ['subject', 'title', 'desciption', 'created_date']


@admin.register(models.Activity)
class ActivityAdmin (admin.ModelAdmin):
    list_display = [
        'title',
        'profile',
        'status',
        'frequency'

    ]


@admin.register(models.Profile)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'user_profile', 'firstName', 'lastName', 'userName', 'age', 'gender'
    ]


@admin.register(models.RoutineGoal)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'status',
        'goal_duration',
        'profile',
        'title',
        'start_date',
        'end_date',
        'created_date',
        'desciption'
    ]


@admin.register(models.Routine)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'activity',
        'title',
        'start_date',
        'end_date',
        'created_date',
        'desciption'
    ]
