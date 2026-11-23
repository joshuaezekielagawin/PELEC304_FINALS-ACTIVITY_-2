# Shiked6 School — Student Enrollment Profiles

A Django app for browsing student enrollment records, searching and filtering the class roster, and viewing each student's personal, academic, and enrollment details. The admin site can be used to manage student records.

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_students
python manage.py createsuperuser
python manage.py runserver
```

Open <http://127.0.0.1:8000/> for the dashboard or <http://127.0.0.1:8000/admin/> for the admin site. The seed command creates fictional sample students and can be run more than once.

## Deploy on PythonAnywhere

### 1. Upload and unpack the ZIP

In PythonAnywhere, open **Files**, upload `shiked6_school_pythonanywhere.zip` to your home directory, then open a Bash console and run:

```bash
mkdir -p ~/shiked6_school
cd ~/shiked6_school
unzip ~/shiked6_school_pythonanywhere.zip
```

The ZIP intentionally excludes the local database and virtual environment. You will create both on PythonAnywhere.

### 2. Create a virtual environment and install Django

Choose a Python version available in the PythonAnywhere Web app setup. Use that same version in the virtual environment; Python 3.13 is a good choice if offered.

```bash
python3.13 -m venv ~/shiked6-venv
source ~/shiked6-venv/bin/activate
pip install -r ~/shiked6_school/requirements.txt
cd ~/shiked6_school
python manage.py migrate
python manage.py seed_students
python manage.py createsuperuser
python manage.py collectstatic --noinput
```

If you chose a version other than Python 3.13, replace `python3.13` with that version's command.

### 3. Create the PythonAnywhere web app

In the **Web** tab, choose **Add a new web app**, select **Manual configuration**, and choose the same Python version as your virtual environment. Set the virtualenv path to `/home/YOURUSERNAME/shiked6-venv` and the source/working directory to `/home/YOURUSERNAME/shiked6_school`.

### 4. Configure the WSGI file

From the Web tab, open the WSGI configuration file linked in the **Code** section. Replace its Django app section with the following, changing `YOURUSERNAME` and setting a private secret key:

```python
import os
import sys

project_path = "/home/YOURUSERNAME/shiked6_school"
if project_path not in sys.path:
    sys.path.insert(0, project_path)

os.environ["DJANGO_SETTINGS_MODULE"] = "enrollment.settings"
os.environ["DJANGO_DEBUG"] = "False"
os.environ["DJANGO_ALLOWED_HOSTS"] = "YOURUSERNAME.pythonanywhere.com"
os.environ["DJANGO_SECRET_KEY"] = "PASTE_A_PRIVATE_RANDOM_SECRET_HERE"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

Generate a private secret in a Bash console with:

```bash
python -c 'import secrets; print(secrets.token_urlsafe(50))'
```

Do not put the secret in the ZIP or share it publicly.

### 5. Configure static files and reload

In the Web tab's **Static files** section, add:

- URL: `/static/`
- Directory: `/home/YOURUSERNAME/shiked6_school/staticfiles`

Then click **Reload** in the Web tab and open `https://YOURUSERNAME.pythonanywhere.com/`. If you later change CSS, JavaScript, or images, rerun `collectstatic --noinput` and reload the web app.

The included sample students are fictional. Back up the database before replacing them with real student records.
