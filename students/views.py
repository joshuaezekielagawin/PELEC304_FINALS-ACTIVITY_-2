from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .models import Student


def dashboard(request, student_id=None):
    query = request.GET.get("q", "").strip()
    section = request.GET.get("section", "all")
    status = request.GET.get("status", "all")

    students = Student.objects.all()
    if query:
        students = students.filter(
            Q(first_name__icontains=query)
            | Q(last_name__icontains=query)
            | Q(student_number__icontains=query)
            | Q(email__icontains=query)
        )
    if section != "all":
        students = students.filter(section=section)
    if status != "all":
        students = students.filter(status=status)

    selected = None
    if student_id is not None:
        selected = get_object_or_404(Student, pk=student_id)
    elif students.exists():
        selected = students.first()
    else:
        selected = Student.objects.first()

    sections = Student.objects.values_list("section", flat=True).distinct().order_by("section")
    context = {
        "students": students,
        "selected": selected,
        "query": query,
        "selected_section": section,
        "selected_status": status,
        "sections": sections,
        "total_students": Student.objects.count(),
        "enrolled_count": Student.objects.filter(status="Enrolled").count(),
        "review_count": Student.objects.filter(status="For Review").count(),
    }
    return render(request, "students/dashboard.html", context)


def home_redirect(request):
    return redirect("students:dashboard")
