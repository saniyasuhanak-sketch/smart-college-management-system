from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from .models import Student
from academics.models import Department, Course


@login_required
def student_list(request):
    query = request.GET.get('q', '')
    qs = Student.objects.select_related('department', 'course')
    if query:
        qs = qs.filter(Q(full_name__icontains=query) | Q(student_id__icontains=query) | Q(email__icontains=query))
    students = qs.order_by('full_name')
    return render(request, 'students/student_list.html', {'students': students, 'query': query})


@login_required
def student_create(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        department_id = request.POST.get('department')
        course_id = request.POST.get('course')
        semester = request.POST.get('semester')
        academic_year = request.POST.get('academic_year')
        address = request.POST.get('address')
        status = request.POST.get('status', 'Active')

        if Student.objects.filter(student_id=student_id).exists():
            messages.error(request, 'Student ID already exists.')
            return render(request, 'students/student_form.html', {'departments': Department.objects.all(), 'courses': Course.objects.all()})

        department = Department.objects.filter(pk=department_id).first()
        course = Course.objects.filter(pk=course_id).first()
        Student.objects.create(
            student_id=student_id,
            full_name=full_name,
            email=email,
            phone=phone,
            department=department,
            course=course,
            semester=semester,
            academic_year=academic_year,
            address=address,
            status=status,
        )
        messages.success(request, 'Student record created successfully.')
        return redirect('students:list')

    return render(request, 'students/student_form.html', {'departments': Department.objects.all(), 'courses': Course.objects.all()})


@login_required
def student_detail(request, pk):
    student = Student.objects.select_related('department', 'course').get(pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})


@login_required
def student_update(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        student.full_name = request.POST.get('full_name')
        student.email = request.POST.get('email')
        student.phone = request.POST.get('phone')
        student.semester = request.POST.get('semester')
        student.academic_year = request.POST.get('academic_year')
        student.status = request.POST.get('status', student.status)
        student.save()
        messages.success(request, 'Student record updated successfully.')
        return redirect('students:detail', pk=student.pk)
    return render(request, 'students/student_edit.html', {'student': student})
