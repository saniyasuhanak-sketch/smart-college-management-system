from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count

from .models import Department, Course, Subject


@login_required
def department_list(request):
    departments = Department.objects.all().order_by('name')
    return render(request, 'academics/departments.html', {'departments': departments})


@login_required
def course_list(request):
    courses = Course.objects.select_related('department').all().order_by('department__name', 'name')
    return render(request, 'academics/courses.html', {'courses': courses})


@login_required
def subject_list(request):
    subjects = Subject.objects.select_related('course').all().order_by('course__name', 'name')
    return render(request, 'academics/subjects.html', {'subjects': subjects})
