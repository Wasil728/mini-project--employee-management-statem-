# Task 15: Employee Management Mini Project (Django)

Employee directory with no database. All employee data lives in `employees/views.py`.

## Run it

```
pip install django
python manage.py runserver
```

Open http://127.0.0.1:8000/

## Pages

| Page | URL |
|---|---|
| Home | `/` |
| Employee list | `/employees/` |
| Employee details | `/employee/101/` (any ID from the list) |
| About | `/about/` |
| Contact | `/contact/` |

## Where each task step lives

| Step | File |
|---|---|
| 1. Employee data | `employees/views.py` (`employees` list) |
| 2. Pass data to template | `employees/views.py` (`employee_list`, `home`) |
| 3. `{% for %}` loop for cards | `employees/templates/employees/employee_list.html` |
| 4. Dynamic URL using Employee ID | `employees/urls.py` (`employee/<int:emp_id>/`) |
| 5. Find employee by ID | `employees/views.py` (`employee_detail`) |
| 6. Separate details template | `employees/templates/employees/employee_detail.html` |
| 7. Profile images in `static` | `employees/static/employees/images/` |
| 8. CSS for cards, navbar, details | `employees/static/employees/css/style.css` |
| Bonus: salary levels | `employees/views.py` (`get_level`) |

To use real photos, drop image files into the images folder and change `profile_image` in the data.
