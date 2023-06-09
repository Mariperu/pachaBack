# Django

## ngrok

HTTP tunnel. It allows sharing my code online.

https://dashboard.ngrok.com/get-started/setup

1. Download ngrok
2. In settings.py, `ALLOWED_HOSTS = ["*"]`
3. Open ngrok zip -> `ngrok http 80`

## django-adminlte3

To customize admin.

_Follow these steps:_ https://github.com/fseesink/django-adminlte3-tutorial

## Django Sign Up and login with confirmation Email

_Follow these steps:_ https://www.geeksforgeeks.org/django-sign-up-and-login-with-confirmation-email-python/

1. `pip install --upgrade django-crispy-forms`

2. `python manage.py startapp user`

3. _settings.py_, add:

```
INSTALLED_APPS = [
....
]


CRISPY_TEMPLATE_PACK = 'bootstrap4'
```
## Generic Views

https://www.geeksforgeeks.org/class-based-generic-views-django-create-retrieve-update-delete/