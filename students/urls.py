from django.urls import path

from . import views

app_name = "students"

urlpatterns = [
    path("", views.home_redirect, name="home"),
    path("students/", views.dashboard, name="dashboard"),
    path("students/<int:student_id>/", views.dashboard, name="detail"),
]
