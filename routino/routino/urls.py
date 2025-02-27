"""routino URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mvp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('myProgress', views.myProgress, name='myProgress'),
    path('profile', views.profile, name='user_profile'),
    path('new-activity', views.new_activity, name=''),
    path('new-goal', views.add_goal, name='goal_form'),
    path('new-routine', views.add_routine, name='routine_form'),
    path('leaderBoard', views.score_calculation, name='score_calculation'),
    path('matches/', views.view_matches, name='view_matches'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# todo : new goal - new routine - overview -> my progress
#       my progress : my goals - my routines - my activities
