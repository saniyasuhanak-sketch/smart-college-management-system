from django.urls import path

from . import views

app_name = 'academics'

urlpatterns = [
    path('departments/', views.department_list, name='departments'),
    path('courses/', views.course_list, name='courses'),
    path('subjects/', views.subject_list, name='subjects'),
]
