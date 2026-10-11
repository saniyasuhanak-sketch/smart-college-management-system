from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Group
from django.db.models import Q

from students.models import Student
from faculty.models import Faculty
from academics.models import Department, Course
from announcements.models import Announcement
from .models import UserProfile


def _user_role(request):
    if request.user.is_authenticated:
        profile = UserProfile.objects.filter(user=request.user).first()
        if profile:
            return profile.role
        if request.user.is_superuser:
            return 'Administrator'
        if request.user.groups.filter(name='Administrator').exists():
            return 'Administrator'
        if request.user.groups.filter(name='Faculty').exists():
            return 'Faculty'
        if request.user.groups.filter(name='Student').exists():
            return 'Student'
    return 'Guest'


def login_view(request):
    if request.user.is_authenticated:
        return redirect('accounts:dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accounts:dashboard')
        messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('accounts:login')


@login_required
def dashboard(request):
    role = _user_role(request)
    cards = {
        'total_students': Student.objects.count(),
        'total_faculty': Faculty.objects.count(),
        'total_departments': Department.objects.count(),
        'total_courses': Course.objects.count(),
    }
    recent_announcements = Announcement.objects.filter(is_active=True).order_by('-published_at')[:5]
    context = {
        'role': role,
        'cards': cards,
        'recent_announcements': recent_announcements,
        'user_profile': UserProfile.objects.filter(user=request.user).first(),
    }
    if role == 'Administrator':
        return render(request, 'accounts/dashboard_admin.html', context)
    if role == 'Faculty':
        return render(request, 'accounts/dashboard_faculty.html', context)
    return render(request, 'accounts/dashboard_student.html', context)


@login_required
def profile_view(request):
    profile = UserProfile.objects.filter(user=request.user).first()
    role = _user_role(request)
    if role == 'Student':
        student = Student.objects.filter(user=request.user).first()
        return render(request, 'accounts/profile_student.html', {'student': student, 'profile': profile})
    if role == 'Faculty':
        faculty = Faculty.objects.filter(user=request.user).first()
        return render(request, 'accounts/profile_faculty.html', {'faculty': faculty, 'profile': profile})
    return render(request, 'accounts/profile_admin.html', {'profile': profile})


@login_required
def change_password(request):
    if request.method == 'POST':
        current = request.POST.get('current_password')
        new = request.POST.get('new_password')
        confirm = request.POST.get('confirm_password')
        if not request.user.check_password(current):
            messages.error(request, 'Current password is incorrect.')
        elif new != confirm:
            messages.error(request, 'New passwords do not match.')
        elif len(new) < 8:
            messages.error(request, 'Password must be at least 8 characters long.')
        else:
            request.user.set_password(new)
            request.user.save()
            messages.success(request, 'Password updated successfully.')
            return redirect('accounts:profile')
    return render(request, 'accounts/change_password.html')
