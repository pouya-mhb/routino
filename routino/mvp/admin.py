from django.contrib import admin
from mvp import models


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


@admin.register(models.Goal)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'status',
        'frequency',
        'profile',
        'start_date',
        'end_date',
        'created_date',
        'desciption'
    ]


@admin.register(models.Routine)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'profile',
        'activity',
        'title',
        'start_date',
        'end_date',
        'created_date',
        'desciption'
    ]
