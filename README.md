# django-team-management-application
Full-Stack take-home assignment


# Pre-requirements:
python 3.5 or later, and:
```
pip intall Django
pip install django-phone-field
```
# Run the team management web app:
Nevigate to the django-team-management-application/my_project folder and run:
```
python manage.py runserver
```
Then, append "/team_management" to the url to be directed to the main page.

# To recreate the team member database if necessary:
Nevigate to the django-team-management-application/my_project folder and run:
```
python manage.py makemigrations team_management
python manage.py migrate
```

# To test the model:
Nevigate to the django-team-management-application/my_project folder, write necessary tests and run:
```
python manage.py test
```