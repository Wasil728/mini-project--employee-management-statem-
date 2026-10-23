from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("employees/", views.employee_list, name="employee_list"),
    path("employee/<int:emp_id>/", views.employee_detail, name="employee_detail"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
