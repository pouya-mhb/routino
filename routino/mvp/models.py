from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Profile (models.Model):
    user_profile = models.OneToOneField(User,
                                        on_delete=models.CASCADE,
                                        primary_key=True,
                                        related_name='user_profile')
    gender_choices = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    firstName = models.CharField(max_length=250, default='user_first_name')
    lastName = models.CharField(max_length=250, default='user_last_name')
    userName = models.CharField(max_length=250)
    age = models.IntegerField(default=18)
    gender = models.CharField(choices=gender_choices, max_length=6)


class Activity (models.Model):
    STATUS_CHOICES = (
        ('new', 'New'),
        ('committed', 'Committed'),
        ('doing', 'Doing'),
        ('done', 'Done'),
    )

    profile = models.ForeignKey(Profile,
                                on_delete=models.CASCADE)

    status = models.CharField(
        max_length=100, choices=STATUS_CHOICES, default='new')

    title = models.CharField(max_length=250)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    desciption = models.TextField()


class Routine (models.Model):
    # def get_profile_id ():
    #     Profile.objects.get(id)

    profile = models.ForeignKey(Profile,
                                on_delete=models.CASCADE,
                                related_name='routine_profile',
                                verbose_name="Routine Profile",
                                default=1)

    activity = models.ForeignKey(
        Activity,
        on_delete=models.CASCADE,
        related_name='routine_activity',
        verbose_name="Routine Activity",
        default=1)

    title = models.CharField(max_length=250)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    desciption = models.TextField()


class RoutineGoal (models.Model):

    STATUS_CHOICES = (
        ('new', 'New'),
        ('committed', 'Committed'),
        ('doing', 'Doing'),
        ('done', 'Done'),
    )

    status = models.CharField(
        max_length=100, choices=STATUS_CHOICES, default='new')

    GOAL_DURATION_CHOICES = (
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('annually', 'Annually'),
    )

    goal_duration = models.CharField(
        max_length=100, choices=GOAL_DURATION_CHOICES, default='0')

    profile = models.ForeignKey(Profile,
                                on_delete=models.CASCADE, default=1)

    routine = models.ForeignKey(Routine,
                                on_delete=models.CASCADE, default=1)

    title = models.CharField(max_length=250)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    desciption = models.TextField()
