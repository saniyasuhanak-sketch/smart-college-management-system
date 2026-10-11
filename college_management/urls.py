from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('accounts/', include('accounts.urls')),
    path('students/', include('students.urls')),
    path('faculty/', include('faculty.urls')),
    path('academics/', include('academics.urls')),
    path('attendance/', include('attendance.urls')),
    path('examinations/', include('examinations.urls')),
    path('fees/', include('fees.urls')),
    path('timetable/', include('timetable.urls')),
    path('announcements/', include('announcements.urls')),
    path('library/', include('library.urls')),
    path('reports/', include('reports.urls')),
]
