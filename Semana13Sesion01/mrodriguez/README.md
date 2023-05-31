# Django - postgreSQL

https://docs.djangoproject.com/es/4.2/intro/tutorial04/

## Testing

### Test unitario

https://docs.djangoproject.com/es/4.2/intro/tutorial05/

1. `python manage.py shell`

   Ejm:

   ```
      >>> import datetime
      >>> from django.utils import timezone
      >>> from polls.models import Question
      >>> # create a Question instance with pub_date 30 days in the future
      >>> future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
      >>> # was it published recently?
      >>> future_question.was_published_recently()
      True
   ```

   ctrl+z + enter 2. config _test.py_ folder

2. `python manage.py test nameApp`

## Adding CSS styles

https://docs.djangoproject.com/es/4.2/intro/tutorial06/

### Styles

1. Create _static/appName/_ folder inside app, then _style.css_ file inside.

2. Add the code inside _templates/Appname/index.html_ file.

```
   {% load static %}

   <link rel="stylesheet" href="{% static 'appName/style.css' %}">
```

3. Verify: `python manage.py runserver`

### Image

1. Create _static/appName/images_ folder inside app, then insert images.

2. Use image, like:

```
body {
    background: white url("images/nameImage.jpg") no-repeat;
}
```

## customizing The Admin

https://docs.djangoproject.com/es/4.2/intro/tutorial07/

- Filters, searcher, join forms in only one interface.
- Templates config

1. Find django base_site.html file: `python -c "import django; print(django.__path__)"`

   It respond with the path: search -> venv/lib/site-packages/django/contrib/admin/templates/admin/base_site.html

   Then can change admin name.
