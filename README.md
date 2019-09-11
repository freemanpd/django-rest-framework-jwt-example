# django-rest-framework-example
An example ["Django REST Framework"](https://www.django-rest-framework.org/) application.

## Screenshots

## Requirements
1. Python 3.4+
1. Pipenv 

## Installation
1. Start Python virtual ENV
```
pipenv shell
```
2. Install dependencies
```
pipenv install
```
3. Run database migrations
```
python3 manage.py migrate
```
4. Create admin user
```
python manage.py createsuperuser --username admin
```

## Run application
```
python manage.py runserver
```
Once the server is running, visit http://127.0.0.1:8000 in your web browser. Now, you should see something like the following:

**Note:** access the Django admin interface here: http://127.0.0.1:8000/admin. Example:

![Django admin login](https://github.com/freemanpd/django-helloworld/blob/master/docs/django-admin-login.png)

## API endpoints


## API examples

## Resources
* Properly installing Python - https://docs.python-guide.org/starting/installation/
* Installing pipenv - https://docs.python-guide.org/dev/virtualenvs/#installing-pipenv
* Django REST Framework - https://www.django-rest-framework.org