from django.db import models
from django.contrib.auth.models import User


class Faculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='faculty_profile', null=True, blank=True)
    faculty_id = models.CharField(max_length=30, unique=True)
    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    department = models.ForeignKey('academics.Department', on_delete=models.SET_NULL, null=True, blank=True, related_name='faculty_members')
    designation = models.CharField(max_length=50, default='Lecturer')
    qualification = models.CharField(max_length=100, blank=True, null=True)
    join_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Active', choices=[('Active','Active'),('Inactive','Inactive')])

    def __str__(self):
        return f'{self.full_name} ({self.faculty_id})'
