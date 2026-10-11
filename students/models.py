from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile', null=True, blank=True)
    student_id = models.CharField(max_length=30, unique=True)
    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    department = models.ForeignKey('academics.Department', on_delete=models.SET_NULL, null=True, blank=True, related_name='students')
    course = models.ForeignKey('academics.Course', on_delete=models.SET_NULL, null=True, blank=True, related_name='students')
    semester = models.PositiveIntegerField(default=1)
    academic_year = models.CharField(max_length=20, default='2025-2026')
    admission_date = models.DateField(auto_now_add=True)
    address = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, default='Active', choices=[('Active','Active'),('Inactive','Inactive'),('Archived','Archived')])

    def __str__(self):
        return f'{self.full_name} ({self.student_id})'
