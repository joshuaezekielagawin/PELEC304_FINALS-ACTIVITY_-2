from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("student_number", models.CharField(max_length=24, unique=True)),
                ("first_name", models.CharField(max_length=80)),
                ("middle_name", models.CharField(blank=True, max_length=80)),
                ("last_name", models.CharField(max_length=80)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=32)),
                ("birth_date", models.DateField()),
                ("gender", models.CharField(max_length=32)),
                ("address", models.TextField()),
                ("guardian_name", models.CharField(max_length=160)),
                ("guardian_phone", models.CharField(max_length=32)),
                ("previous_school", models.CharField(max_length=180)),
                ("grade_level", models.CharField(max_length=40)),
                ("section", models.CharField(max_length=80)),
                ("school_year", models.CharField(max_length=20)),
                ("enrollment_date", models.DateField()),
                ("status", models.CharField(choices=[("Enrolled", "Enrolled"), ("For Review", "For Review"), ("Pending", "Pending")], default="Enrolled", max_length=24)),
                ("gpa", models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ("notes", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["last_name", "first_name"]},
        ),
    ]
