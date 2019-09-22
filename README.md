# django-rest-framework-example
An example ["Django REST framework"](https://www.django-rest-framework.org/) JSON Web Token ["(JWT)"](https://en.wikipedia.org/wiki/JSON_Web_Token) application.

[![Build Status](https://travis-ci.com/freemanpd/django-rest-framework-jwt-example.svg?branch=master)](https://travis-ci.com/freemanpd/django-rest-framework-jwt-example)

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
python manage.py migrate
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

![Django admin login](https://github.com/freemanpd/django-rest-framework-jwt-example/blob/master/docs/django-admin-login.png)

## Endpoints
* ```api/v1/```
* ```api/token/```
* ```api/token/refresh/```
* ```health_check/```
![health_check](https://github.com/freemanpd/django-rest-framework-jwt-example/blob/master/docs/health_check.png)
## API/endpoint examples

### Obtain token
```
curl -XPOST http://localhost:8000/api/token/  -H "Content-Type: application/json" -d '{"username": "admin", "password": "password123"}' 

...
{"refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYwMDEwMjU4NywianRpIjoiMjE3NmE1MTNhMTIyNDM5MmEwMTk0NDlhY2ZjNzg0NGIiLCJ1c2VyX2lkIjoxfQ.RjXDUt90_W7t6N-h4P333clLbQ5oDLHSS3suQ56w1_Q","access":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAwMTAyNTg3LCJqdGkiOiI4ZmY0YjVkMTNmMTY0MDk4YjVmMGE2MmUwMTRhMGUwZSIsInVzZXJfaWQiOjF9.pOof6NyWHSfFVcJrJhpQMlAEzFKpyR9aTj-og_OpVaE"}
```

### Create content

![rest](https://github.com/freemanpd/django-rest-framework-jwt-example/blob/master/docs/rest.png)

### Retrieve content
```
curl -XGET http://localhost:8000/api/v1/ -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAwMTAzMjI2LCJqdGkiOiIzZTJiMWNmMzI1YTc0YjNhOTA2OGEwYWI0Y2IxNWJkMCIsInVzZXJfaWQiOjF9.BPjzsKgIWrgRn-qwjqCklKQ52KEJOnVjPNULE58MbkM" 
```

### Check appliction health
``` curl -XGET http://localhost:8000/health_check/?format=json ```

## Resources
* Properly installing Python - https://docs.python-guide.org/starting/installation/
* Installing pipenv - https://docs.python-guide.org/dev/virtualenvs/#installing-pipenv
* Django REST Framework - https://www.django-rest-framework.org
* Django REST Framework Simple JWT - https://github.com/davesque/django-rest-framework-simplejwt
