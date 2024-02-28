from django.http import HttpResponse
from django.http.response import HttpResponseBadRequest
from django.shortcuts import render, redirect
from .forms import Routineform, GoalForm, ActivityForm, LoginForm, ProfileForm, RegisterForm
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
        profile_builder(request, user)

        return redirect('login')
    else:
        userRegisterForm = RegisterForm()
        return render(request, "Register.html", {"RegisterForm": userRegisterForm, 'title': 'Register'})


def profile_builder(request, user):

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
    current_user = request.user
    goals = Goal.objects.all()
    users = User.objects.all()
    profiles = Profile.objects.all()
    routines = Routine.objects.all()
    activities = Activity.objects.all()

    home_context = {
        'current_user': current_user,
        'users': users,
        'goals': goals,
        'profiles': profiles,
        'routines': routines,
        'activities': activities
    }

    # overall_score =

    return render(request, "Home.html", home_context)


@login_required
def profile(request):
    current_user = request.user
    profile = Profile.objects.get(user_profile=current_user)

    profile_context = {
        'user_fullname': f"{profile.firstName} {profile.lastName}",
        'username': profile.userName,
        'age': profile.age,
        'gender': profile.gender
    }

    if request.method == 'post':
        pass
    else:
        return render(request, "Profile.html", profile_context)


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


def score_calculation(request):
    profiles = Profile.objects.all()
    activities = Activity.objects.all()
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    frequencies = Frequency.objects.all()
    statuses = Status.objects.all()

    for profile in profiles:
        for activity in activities:
            for category in categories:
                for subCategory in subcategories:
                    for frequency in frequencies:
                        for status in statuses:
                            # username = profile.userName
                            status_score = status.score
                            category_score = category.score
                            subcategory_score = subCategory.score
                            frequency_score = frequency.score
                            activity_score = category_score * \
                                subcategory_score * status_score * frequency_score

    score_context = {
        'profiles': profiles,
        'activities': activities,
        'category_score': category_score,
        'sub_category_score': subcategory_score,
        'status_score': status_score,
        'frequency_score': frequency_score,
        'activity_score': activity_score
    }

    return render(
        request, 'LeaderBoard.html', score_context)
