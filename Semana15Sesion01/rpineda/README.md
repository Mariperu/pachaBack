# Django Rest Framework

1. https://cosasdedevs.com/posts/como-crear-una-api-completa-con-django-rest-framework/

2. https://cosasdedevs.com/posts/registro-y-autenticacion-con-django-rest-framework/

3. https://cosasdedevs.com/posts/creacion-lectura-actualizacion-y-borrado-con-django-rest-framework/

Test API

http://127.0.0.1:8000/users/login/

use token after login, if is required.

## Init set up

1.  `python -m venv venv`

2.  `source venv/Scripts/activate`

3.  `python -m pip install Django`

4.  `django-admin startproject projectName .`

5.  `python -m pip install ...`: Markdown, django-filter, djangorestframework, psycopg2, django-ckeditor, Pillow, python-dotenv.

6.  Set up _.env_ file.

7.  _settings.py_ (import _os_ and _dotenv_)

    ```
    INSTALLED_APPS = [
        ...
        'rest_framework',
        'ckeditor',
    ]

    DATABASES = {
        'default': {...}
    }

    SECRET_KEY = os.environ['SECRET_KEY']
    DEBUG = os.environ['DEBUG']

    MEDIA_ROOT = os.path.join(BASE_DIR, "media")
    MEDIA_URL = "/media/"

    # ******* if exists an app like users or other to use in others apps, call it as:
    AUTH_USER_MODEL = 'users.User'

    ```

8.  `python manage.py startapp appName`

    Add app in _settings.py_ file.

9.  Set up _models.py_ in app.

10. `python manage.py makemigrations appName`

11. `python manage.py migrate`

12. Register model in _admin.py_ file.

13. Create and set up _serializers.py_ in app folder.

14. Set up _views.py_

15. Create and set up _urls.py_.

16. `py manage.py createsuperuser`

17. `python manage.py runserver`

18. Test APIs: localhost:8000/api/...
