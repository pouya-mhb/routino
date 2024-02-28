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

    def __str__(self):
        return self.userName


class Category (models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    score = models.IntegerField(default=1)
    created_date = models.DateTimeField(default=timezone.now)

    # score = models.IntegerField(default=1)

    # category_choices = (
    #     ('sport', 'sport'),
    #     ('health', 'health'),
    #     ('self-development', 'self-development')
    # )

    # category = models.CharField(
    #     max_length=100, choices=category_choices, default='-')

    # category_choices_score = (
    #     ('sport', 100),
    #     ('mindset', 100),
    #     ('self-development', 80)
    # )

    # score = models.CharField(
    #     max_length=100, choices=category_choices_score, default='-')

    # category_choices_item = models.CharField(
    #     max_length=250, verbose_name='category_item')
    # def choices(category_choices_item):
    #     choice_list = []
    #     choice_list.append(category_choices_item)
    #     return choice_list

    def __str__(self) -> str:
        return self.title


class Status (models.Model):
    # STATUS_CHOICES = (
    #     ('new', 'New'),
    #     ('committed', 'Committed'),
    #     ('doing', 'Doing'),
    #     ('done', 'Done'),
    # )

    # title = models.CharField(
    #     max_length=100, choices=STATUS_CHOICES, default='new')

    title = models.CharField(max_length=250)
    score = models.IntegerField(default=1)
    description = models.TextField(max_length=250, default='')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Frequency (models.Model):
    title = models.CharField(max_length=250)
    score = models.IntegerField(default=1)
    description = models.TextField(max_length=250, default='')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    # FREQUENCY_CHOICES = (
    #     ('always', 'always'),
    #     ('usually', 'usually'),
    #     ('often', 'often'),
    #     ('sometimes', 'sometimes'),
    # )

    # title = models.CharField(
    #     max_length=100, choices=FREQUENCY_CHOICES, default='always'
    # )

    # FREQUENCY_SCORE_CHOICES = (
    #     ('always', 100),
    #     ('usually', 80),
    #     ('often', 50),
    #     ('sometimes', 30),
    # )

    # score = models.CharField(
    #     max_length=100, choices=FREQUENCY_SCORE_CHOICES, default='always'
    # )


class SubCategory(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    score = models.IntegerField(default=1)
    description = models.TextField(max_length=250, default='')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    # type_choices = (
    #     ('exercising', 'exercising'),
    #     ('running', 'running'),
    #     ('cycling', 'cycling'),
    #     ('gym', 'gym'),
    #     ('green diet', 'green diet'),
    #     ('low fat diet', 'low fat diet'),
    #     ('only meet diet', 'only meet diet'),
    #     ('studying', 'studying'),
    #     ('reading', 'reading'),
    #     ('attending courses', 'attending courses')
    # )

    # title = models.CharField(
    #     max_length=100, choices=type_choices, default='')

    # type_choices_score = (
    #     ('exercising', 10),
    #     ('running', 10),
    #     ('cycling', 15),
    #     ('gym', 20),
    #     ('green diet', 30),
    #     ('low fat diet', 35),
    #     ('only meet diet', 100),
    #     ('studying', 1000),
    #     ('reading', 500),
    #     ('attending courses', 700)
    # )

    # type_score = models.CharField(
    #     max_length=100, choices=type_choices_score, default='')


class Activity (models.Model):
    profile = models.ForeignKey(Profile,
                                on_delete=models.CASCADE)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    frequency = models.ForeignKey(Frequency, on_delete=models.CASCADE)

    title = models.CharField(max_length=250)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    # def activity_score_calculator(request, frequency_score, category_score, status_score, type_score):
    #     activity_score = frequency_score * category_score * status_score * type_score

    #     return activity_score

    # score = activity_score_calculator(
    #     Frequency().objects.filter(), Category().objects.get('score'), Status().objects.get('score'), Type.objects.get('score'))

    def __str__(self):
        return self.title


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

    def __str__(self):
        return self.title


class Goal(models.Model):

    # STATUS_CHOICES = (
    #     ('new', 'New'),
    #     ('committed', 'Committed'),
    #     ('doing', 'Doing'),
    #     ('done', 'Done'),
    # )

    # status = models.CharField(
    #     max_length=100, choices=STATUS_CHOICES, default='new')

    # GOAL_DURATION_CHOICES = (
    #     ('daily', 'Daily'),
    #     ('weekly', 'Weekly'),
    #     ('monthly', 'Monthly'),
    #     ('annually', 'Annually'),
    # )

    # frequency = models.CharField(
    #     max_length=100, choices=GOAL_DURATION_CHOICES, default='0')

    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE, default=1)

    type = models.ForeignKey(SubCategory,
                             on_delete=models.CASCADE, default=1)

    status = models.ForeignKey(Status,
                               on_delete=models.CASCADE, default=1)

    status = models.ForeignKey(Frequency,
                               on_delete=models.CASCADE, default=1)

    routine = models.ForeignKey(Routine,
                                on_delete=models.CASCADE, default=1)

    profile = models.ForeignKey(Profile,
                                on_delete=models.CASCADE, default=1)

    activity = models.ForeignKey(
        Activity,
        on_delete=models.CASCADE,
        default=1)

    title = models.CharField(max_length=250)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    desciption = models.TextField()

    def __str__(self):
        return self.title
