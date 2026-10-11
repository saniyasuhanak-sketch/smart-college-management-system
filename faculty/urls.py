from django.urls import path

from . import views

app_name = 'faculty'

urlpatterns = [
    path('', views.faculty_list, name='list'),
    path('add/', views.faculty_create, name='add'),
    path('<int:pk>/', views.faculty_detail, name='detail'),
    path('<int:pk>/edit/', views.faculty_update, name='edit'),
]
