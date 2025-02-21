from django.http import HttpResponse
from django.http.response import HttpResponseBadRequest
from django.shortcuts import render, redirect
from .forms import RoutineForm, GoalForm, ActivityForm, LoginForm, ProfileForm, RegisterForm
from .models import Profile, Activity, Routine, Goal, Category, SubCategory, Frequency, Status
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone


def register(request):
    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username, email, password)
        user.first_name = firstName
        user.last_name = lastName
        user.save()
        profile_builder(user)

        return redirect('login')
    else:
        userRegisterForm = RegisterForm()
        return render(request, "Register.html", {"RegisterForm": userRegisterForm, 'title': 'Register'})


def profile_builder(user):
    user_profile = Profile.objects.create(
        user_profile=user, firstName=user.first_name, lastName=user.last_name, userName=user.username)
    user_profile.save()


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.add_message(request, messages.INFO,
                                 "wrong user / pass")
            return redirect('login')
    else:
        LoginForm()
        return render(request, "login.html", {
            "loginForm": LoginForm
        })


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def get_home(request):
    if request.user.is_authenticated:
        current_user = request.user
        context = {
            'user_fullname': f"{current_user.first_name} {current_user.last_name}"
        }
    return render(request, "home.html", context)


def home(request):
    # current_user = request.user
    # goals = Goal.objects.all()
    # users = User.objects.all()
    # routines = Routine.objects.all()
    profiles = Profile.objects.all()
    activities = Activity.objects.all()
    for activity in activities:
        activity_score = activity.frequency.score * activity.status.score * \
            activity.category.score * activity.type.score

    home_context = {
        # 'current_user': current_user,
        # 'users': users,
        # 'goals': goals,
        # 'profiles': profiles,
        # 'routines': routines,
        'activities': activities,
        # 'activity_score': activity_score
    }

    # overall_score =

    return render(request, "Home.html", home_context)

@login_required
def profile(request):
    current_user = request.user
    profile = Profile.objects.get(user_profile=current_user)
    profile_form = ProfileForm(instance=profile)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')
        else:
            messages.error(request, 'Error updating your profile')

    goals = Goal.objects.filter(profile=profile)
    routines = Routine.objects.filter(profile=profile)
    activities = Activity.objects.filter(profile=profile)

    get_profile_context = {
        'user_fullname': f"{profile.firstName} {profile.lastName}",
        'username': profile.userName,
        'age': profile.age,
        'profile_form': profile_form,
        'gender': profile.gender,
        'goals': goals,
        'routines': routines,
        'activities': activities,
        'activity_score': profile.activity_score,
        'frequency_score': profile.frequency_score,
        'status_score': profile.status_score,
        'overall_score': profile.overall_score,
    }
    return render(request, "Profile.html", get_profile_context)


@login_required
def myProgress(request):
    current_user = request.user

    goals = Goal.objects.filter(
        profile=Profile.objects.get(user_profile=current_user))

    routines = Routine.objects.filter(
        profile=Profile.objects.get(user_profile=current_user))

    activities = Activity.objects.filter(
        profile=Profile.objects.get(user_profile=current_user))

    for activity in activities:
        activity_score = activity.frequency.score * activity.status.score * \
            activity.category.score * activity.type.score

    context = {
        'user_fullname': f"{current_user.first_name} {current_user.last_name}",
        'goals': goals,
        'routines': routines,
        'activities': activities,
        'activity_score': activity_score
    }

    return render(
        request, 'MyProgress.html', context)


@login_required
def new_activity(request):
    if request.method == 'POST':
        activity_form = ActivityForm(request.POST)
        if activity_form.is_valid():
            activity = activity_form.save(commit=False)
            activity.profile = request.user.user_profile
            activity.save()
            messages.success(request, 'New activity added successfully')
            return redirect('user_profile')
            # return redirect('activity_list')  # ToDo
        else:
            messages.error(request, 'Error adding new activity')
    else:
        activity_form = ActivityForm()

    return render(request, 'new-activity.html', {'activity_form': activity_form})

@login_required
def add_goal(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            # Set the profile to the currently logged-in user's profile
            goal.profile = request.user.user_profile
            goal.save()
            return redirect('user_profile')
            # return redirect('goal_list')  # ToDO
    else:
        form = GoalForm()
    return render(request, 'goal_form.html', {'form': form})

@login_required
def add_routine(request):
    if request.method == 'POST':
        form = RoutineForm(request.POST)
        if form.is_valid():
            routine = form.save(commit=False)
            # Set the routine's profile to the current user's profile
            routine.profile = request.user.user_profile
            routine.save()
            return redirect('user_profile')  # Change to your desired URL name
            # return redirect('routine_list')  # Change to your desired URL name
    else:
        form = RoutineForm()
    return render(request, 'routine_form.html', {'form': form})


def match_making(user, routine):
    # if type_user_routine_1 = type_user_routine_2
    # if requency_user_routine_1 = requency_user_routine_2
    # user_1 match to user_2

    pass

def score_calculation(request):
    profiles = Profile.objects.all()
    activities = Activity.objects.all()

    for profile in profiles:
        profile.activity_score = 0
        profile.frequency_score = 0
        profile.status_score = 0
        profile.overall_score = 0

        user_activities = activities.filter(profile=profile)
        for activity in user_activities:
            profile.activity_score += activity.score
            profile.frequency_score += activity.frequency.score
            profile.status_score += activity.status.score

        profile.overall_score = profile.activity_score + profile.frequency_score + profile.status_score

    score_context = {
        'profiles': profiles,
        'activities': activities,
    }

    return render(request, 'LeaderBoard.html', score_context)