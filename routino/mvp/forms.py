from django import forms
from django.contrib.auth.models import User
from django.db.models import fields
from django.forms.models import ModelForm
from .models import Profile, Activity, Routine, Goal


class ActivityForm(ModelForm):
    class Meta():
        model = Activity
        fields = [
            'profile',
            'category',
            'type',
            'status',
            'frequency',
            'title',
            'start_date',
            'end_date',
            'description',
            'score'
        ]


class ProfileForm (ModelForm):
    class Meta():
        model = Profile
        fields = [
            'firstName', 'lastName', 'userName', 'age', 'gender'
        ]


class RegisterForm(ModelForm):
    class Meta():
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password'
        ]


class LoginForm(ModelForm):
    username = forms.CharField(
        max_length=200, min_length=4, required=True, label='User Name',
        widget=forms.TextInput(
            attrs={'id': 'username',
                   'class': 'form-control',
                   'placeholder': 'Paul_Anderson'}
        )
    )
    password = forms.CharField(
        max_length=200, min_length=4, required=True, label='Password',
        widget=forms.TextInput(
            attrs={'id': 'password',
                   'class': 'form-control',
                   'type': 'password',
                   'placeholder': '*123QWE@ewq*'}
        )
    )

    class Meta():
        model = User
        fields = [
            'username',
            'password'
        ]


class RoutineForm (ModelForm):
    class Meta():
        model = Routine
        fields =  ['activity', 'title', 'start_date', 'end_date', 'description']


class GoalForm (ModelForm):
    class Meta():
        model = Goal
        fields = [
            'routine', 'category', 'subCategory', 'status', 'activity', 'title', 'start_date', 'end_date', 'description'
        ]
