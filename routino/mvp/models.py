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


class SubCategory(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    score = models.IntegerField(default=1)
    description = models.TextField(max_length=250, default='')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


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

    # score = Category.objects.get() * SubCategory.score * \
    #     Frequency.score * Status.score

    def __str__(self):
        return self.title

    # def score_calculation():

    #     activities = Activity.objects.all()
    #     categories = Category.objects.all()
    #     subcategories = SubCategory.objects.all()
    #     frequencies = Frequency.objects.all()
    #     statuses = Status.objects.all()

    #     for activity in activities:
    #         for category in categories:
    #             for subCategory in subcategories:
    #                 for frequency in frequencies:
    #                     for status in statuses:
    #                         status_score = status.score
    #                         category_score = category.score
    #                         subcategory_score = subCategory.score
    #                         frequency_score = frequency.score
    #                         activity_score = category_score * \
    #                             subcategory_score * status_score * frequency_score
    #     return activity_score

    def __str__(self):
        return self.title


class Routine (models.Model):
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


class Goal(models.Model):
    profile = models.ForeignKey(Profile,
                                on_delete=models.CASCADE, default=1)

    routine = models.ForeignKey(Routine,
                                on_delete=models.CASCADE, default=1)

    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE, default=1)

    subCategory = models.ForeignKey(SubCategory,
                                    on_delete=models.CASCADE, default=1)

    status = models.ForeignKey(Status,
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
