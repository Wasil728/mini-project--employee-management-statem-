from django.http import Http404
from django.shortcuts import render

# ---------------------------------------------------------------------------
# Step 1: Employee data lives here, so the project needs no database.
# "profile_image" is a file inside employees/static/employees/images/
# ---------------------------------------------------------------------------
employees = [
    {
        "id": 101,
        "name": "Aarav Sharma",
        "department": "Engineering",
        "designation": "Backend Developer",
        "salary": 62000,
        "experience": 5,
        "city": "Bhopal",
        "profile_image": "emp101.svg",
        "status": "Active",
    },
    {
        "id": 102,
        "name": "Priya Verma",
        "department": "Design",
        "designation": "UI/UX Designer",
        "salary": 46000,
        "experience": 3,
        "city": "Indore",
        "profile_image": "emp102.svg",
        "status": "Active",
    },
    {
        "id": 103,
        "name": "Rohan Mehta",
        "department": "Marketing",
        "designation": "Marketing Executive",
        "salary": 28000,
        "experience": 1,
        "city": "Jabalpur",
        "profile_image": "emp103.svg",
        "status": "Active",
    },
    {
        "id": 104,
        "name": "Sneha Patel",
        "department": "Human Resources",
        "designation": "HR Manager",
        "salary": 50000,
        "experience": 7,
        "city": "Bhopal",
        "profile_image": "emp104.svg",
        "status": "Active",
    },
    {
        "id": 105,
        "name": "Imran Khan",
        "department": "Engineering",
        "designation": "Frontend Developer",
        "salary": 41000,
        "experience": 2,
        "city": "Pune",
        "profile_image": "emp105.svg",
        "status": "On Leave",
    },
    {
        "id": 106,
        "name": "Neha Joshi",
        "department": "Finance",
        "designation": "Accountant",
        "salary": 30000,
        "experience": 4,
        "city": "Indore",
        "profile_image": "emp106.svg",
        "status": "Active",
    },
    {
        "id": 107,
        "name": "Vikram Singh",
        "department": "Sales",
        "designation": "Sales Associate",
        "salary": 24000,
        "experience": 1,
        "city": "Nagpur",
        "profile_image": "emp107.svg",
        "status": "Active",
    },
    {
        "id": 108,
        "name": "Ananya Iyer",
        "department": "Engineering",
        "designation": "QA Engineer",
        "salary": 36000,
        "experience": 2,
        "city": "Hyderabad",
        "profile_image": "emp108.svg",
        "status": "Active",
    },
]


# ---------------------------------------------------------------------------
# Bonus logic: classify an employee by salary.
# ---------------------------------------------------------------------------
def get_level(salary):
    if salary >= 50000:
        return "Senior Level"
    elif salary >= 30000:
        return "Mid Level"
    else:
        return "Junior Level"


# Add a "level" to every employee once, when the server starts.
for emp in employees:
    emp["level"] = get_level(emp["salary"])


# ---------------------------------------------------------------------------
# Views
# ---------------------------------------------------------------------------
def home(request):
    context = {
        "featured": employees[:3],
        "total": len(employees),
        "active": sum(1 for emp in employees if emp["status"] == "Active"),
        "departments": len({emp["department"] for emp in employees}),
        "cities": len({emp["city"] for emp in employees}),
    }
    return render(request, "employees/home.html", context)


# Step 2: pass `employees` from views.py to the template.
def employee_list(request):
    return render(request, "employees/employee_list.html", {"employees": employees})


# Steps 4 and 5: the URL carries the Employee ID (/employee/101/),
# and the view uses that ID to find the selected employee.
def employee_detail(request, emp_id):
    selected = None
    for emp in employees:
        if emp["id"] == emp_id:
            selected = emp
            break

    if selected is None:
        raise Http404("No employee with that ID.")

    return render(request, "employees/employee_detail.html", {"employee": selected})


def about(request):
    return render(request, "employees/about.html")


def contact(request):
    context = {}
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()

        if name and email and message:
            # Nothing is stored: there is no database in this project.
            context["sent_name"] = name
        else:
            context["error"] = "Fill in your name, email and message."
            context["values"] = {"name": name, "email": email, "message": message}

    return render(request, "employees/contact.html", context)
