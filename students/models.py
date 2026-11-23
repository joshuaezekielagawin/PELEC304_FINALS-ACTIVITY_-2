from django.db import models


class Student(models.Model):
    STATUS_CHOICES = [
        ("Enrolled", "Enrolled"),
        ("For Review", "For Review"),
        ("Pending", "Pending"),
    ]

    student_number = models.CharField(max_length=24, unique=True)
    first_name = models.CharField(max_length=80)
    middle_name = models.CharField(max_length=80, blank=True)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    phone = models.CharField(max_length=32)
    birth_date = models.DateField()
    gender = models.CharField(max_length=32)
    address = models.TextField()
    guardian_name = models.CharField(max_length=160)
    guardian_phone = models.CharField(max_length=32)
    previous_school = models.CharField(max_length=180)
    grade_level = models.CharField(max_length=40)
    section = models.CharField(max_length=80)
    school_year = models.CharField(max_length=20)
    enrollment_date = models.DateField()
    status = models.CharField(max_length=24, choices=STATUS_CHOICES, default="Enrolled")
    gpa = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = "student"
        verbose_name_plural = "students"

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

    @property
    def full_name(self):
        return " ".join(part for part in [self.first_name, self.middle_name, self.last_name] if part)

    @property
    def initials(self):
        return f"{self.first_name[:1]}{self.last_name[:1]}".upper()

    @property
    def avatar_tone(self):
        tones = ["violet", "cyan", "coral", "mint", "gold"]
        return tones[self.pk % len(tones)] if self.pk else tones[0]
