from django.http import HttpResponse
from django.http.response import HttpResponseBadRequest
from django.shortcuts import render, redirect
from .forms import Routineform, RoutineGoalForm, ActivityForm, LoginForm, ProfileForm, RegisterForm
from .models import Profile, Activity, Routine, RoutineGoal
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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

        user_profile = Profile.objects.create(
            user_profile=user, firstName=firstName, lastName=lastName, userName=username)
        user_profile.save()

        return redirect('login')
    else:
        userRegisterForm = RegisterForm()
        return render(request, "Register.html", {"RegisterForm": userRegisterForm, 'title': 'Register'})


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
    current_user = request.user
    goals = RoutineGoal.objects.all()
    users = User.objects.all()
    profiles = Profile.objects.all()
    routines = Routine.objects.all()
    activities = Activity.objects.all()

    home_context = {
        'users': users,
        'goals': goals,
        'profiles': profiles,
        'routines': routines,
        'activities': activities
    }

    return render(request, "Home.html", home_context)


@login_required
def myProgress(request):
    current_user = request.user
    context = {
        'user_fullname': f"{current_user.first_name} {current_user.last_name}",
        # 'activities': Activity.objects.filter(profile=Profile.objects.get(user_profile=current_user)),
        # 'routines': Routine.objects.filter(profile=Profile.objects.get(user_profile=current_user)),
        # nothing is binded to user, everything is binded to profile
        # todo : create profile when user has been registered
    }
    return render(
        request, 'MyProgress.html', context)


# def new_activity(request):
#     if request.method == 'GET':
#         activity_form = Activity()
#         return render(request, " new-activity.html", {"activity_form": activity_form})

#     elif request.method == 'POST':
#         activity_form = ActivityForm(request.POST)
#         if activity_form.is_valid() and request.user.is_authenticated:
#             current_user = request.user
#             activity = activity_form.save(commit=False)
#             activity.user = current_user
#             activity.save()
#             print(request.POST)
#             return redirect("overview")
#         else:
#             return HttpResponseBadRequest()

def match_making(user, routine):
    # if type_user_routine_1 = type_user_routine_2
    # if requency_user_routine_1 = requency_user_routine_2
    # user_1 match to user_2

    pass

    # todo : profile builder
