from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("students", "0001_initial")]
    operations = [
        migrations.AlterField(
            model_name="student",
            name="gpa",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
