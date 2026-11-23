<<<<<<< HEAD
# PELEC304_FINALS-ACTIVITY_-2
FINALS ACTIVITY #2: Develop a Profile View of Students for an Online Enrollment System. For this activity, you will need to develop a Profile View for an Online Enrollment System that shows a list of students and whenever I click one, it will show it's specific information (e.g. Personal Info, Background Info, etc.)
=======
# Classmate — Student Enrollment Profile View

A Django-based admin dashboard for viewing students in a class. The interface uses a soft glassmorphism visual system and lets an admin search, filter, and click any student to inspect personal, background, and enrollment information.

## Local setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_students
python manage.py runserver
```

Open http://127.0.0.1:8000/.

## PythonAnywhere deployment

1. Create a PythonAnywhere account and a new **Web** app using **Manual configuration** and Python 3.10+.
2. Upload this folder (or clone its repository) into `/home/<your-username>/student_enrollment`.
3. Open a Bash console and run:
   ```bash
   cd ~/student_enrollment
   python3.10 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py seed_students
   python manage.py collectstatic --noinput
   ```
4. In the Web tab, set the source directory to `/home/<your-username>/student_enrollment`.
5. Set the WSGI file to:
   `/home/<your-username>/student_enrollment/enrollment/wsgi.py`
6. In the WSGI file, update the project path if needed:
   ```python
   import sys
   path = '/home/<your-username>/student_enrollment'
   if path not in sys.path:
       sys.path.append(path)
   ```
7. Set the virtualenv to `/home/<your-username>/student_enrollment/.venv` and reload the web app.
8. For production, set `DJANGO_DEBUG=False`, a strong `DJANGO_SECRET_KEY`, and `DJANGO_ALLOWED_HOSTS=<your-username>.pythonanywhere.com` in the Web app environment variables.

The app is intentionally seeded with fictional demo records for classroom presentation. Replace them with real database records before production use.
>>>>>>> master
