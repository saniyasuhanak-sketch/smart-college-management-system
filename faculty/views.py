from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from .models import Faculty
from academics.models import Department


@login_required
def faculty_list(request):
    query = request.GET.get('q', '')
    qs = Faculty.objects.select_related('department')
    if query:
        qs = qs.filter(Q(full_name__icontains=query) | Q(faculty_id__icontains=query) | Q(email__icontains=query))
    faculty = qs.order_by('full_name')
    return render(request, 'faculty/faculty_list.html', {'faculty': faculty, 'query': query})


@login_required
def faculty_create(request):
    if request.method == 'POST':
        faculty_id = request.POST.get('faculty_id')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        department_id = request.POST.get('department')
        designation = request.POST.get('designation')
        qualification = request.POST.get('qualification')
        status = request.POST.get('status', 'Active')

        if Faculty.objects.filter(faculty_id=faculty_id).exists():
            messages.error(request, 'Faculty ID already exists.')
            return render(request, 'faculty/faculty_form.html', {'departments': Department.objects.all()})

        department = Department.objects.filter(pk=department_id).first()
        Faculty.objects.create(
            faculty_id=faculty_id,
            full_name=full_name,
            email=email,
            phone=phone,
            department=department,
            designation=designation,
            qualification=qualification,
            status=status,
        )
        messages.success(request, 'Faculty member added successfully.')
        return redirect('faculty:list')

    return render(request, 'faculty/faculty_form.html', {'departments': Department.objects.all()})


@login_required
def faculty_detail(request, pk):
    faculty = Faculty.objects.select_related('department').get(pk=pk)
    return render(request, 'faculty/faculty_detail.html', {'faculty': faculty})


@login_required
def faculty_update(request, pk):
    faculty = Faculty.objects.get(pk=pk)
    if request.method == 'POST':
        faculty.full_name = request.POST.get('full_name')
        faculty.email = request.POST.get('email')
        faculty.phone = request.POST.get('phone')
        faculty.designation = request.POST.get('designation')
        faculty.qualification = request.POST.get('qualification')
        faculty.status = request.POST.get('status', faculty.status)
        faculty.save()
        messages.success(request, 'Faculty record updated successfully.')
        return redirect('faculty:detail', pk=faculty.pk)
    return render(request, 'faculty/faculty_edit.html', {'faculty': faculty})
