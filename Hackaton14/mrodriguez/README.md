# Admin django - adminlte3

## setup:

1. `python -m venv venv`
2. `source venv/Scripts/activate`
3. `python -m pip install Django`
4. `django-admin startproject projectName .`
5. `pip install django-adminlte3`
6. _settings.py_

   ```
   INSTALLED_APPS = [
    'adminlte3',
    'adminlte3_theme',
    ...
   ]
   ```

   ```
   STATIC_ROOT = os.path.join(BASE_DIR, "static")
   ```

7. `python manage.py collectstatic`
8. `python manage.py migrate`
9. `python manage.py runserver`
10. `python manage.py createsuperuser`
11. `python manage.py startapp appName`

    _settings.py_

    ```
    INSTALLED_APPS = [
    ...,
    "blog.apps.BlogConfig",
    ]
    ```

12. _models.py_
13. `python manage.py makemigrations appName`
14. `python manage.py migrate`
15. Add models in _admin.py_
16. `python manage.py runserver`
