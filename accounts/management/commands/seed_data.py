from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

User = get_user_model()


class Command(BaseCommand):
    help = 'Seed demo users, roles, and sample data for the College Management System.'

    def handle(self, *args, **options):
        groups = ['Administrator', 'Faculty', 'Student']
        for name in groups:
            Group.objects.get_or_create(name=name)

        admin_user, created = User.objects.get_or_create(username='admin', defaults={'is_staff': True, 'is_superuser': True})
        if created:
            admin_user.set_password('admin123')
            admin_user.save()
        admin_user.groups.clear()
        admin_user.groups.add(Group.objects.get(name='Administrator'))

        # create sample faculty and student users if not present
        faculty_user, _ = User.objects.get_or_create(username='faculty', defaults={'is_staff': True})
        faculty_user.set_password('faculty123')
        faculty_user.save()
        faculty_user.groups.clear()
        faculty_user.groups.add(Group.objects.get(name='Faculty'))

        student_user, _ = User.objects.get_or_create(username='student', defaults={})
        student_user.set_password('student123')
        student_user.save()
        student_user.groups.clear()
        student_user.groups.add(Group.objects.get(name='Student'))

        self.stdout.write(self.style.SUCCESS('Demo roles and users created successfully.'))
