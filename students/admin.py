from django.contrib import admin

from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_number", "full_name", "grade_level", "section", "status", "enrollment_date")
    list_filter = ("grade_level", "section", "status", "school_year")
    search_fields = ("student_number", "first_name", "last_name", "email")
    ordering = ("last_name", "first_name")
