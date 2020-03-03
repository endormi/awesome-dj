# Django-Bootstrap-Boilerplate [![Travis (.org) branch](https://img.shields.io/travis/endormi/awesome-dj/travis-test-bp)](https://travis-ci.org/endormi/awesome-dj)

Boilerplate for Django using Bootstrap **4.3.1**

> Easy-to-use Boilerplate. Including four **HTML** templates `base.html`, `index.html`, `about.html` and `contact.html`. The db used is `sqlite3`.

> Django [databases](https://docs.djangoproject.com/en/3.0/ref/databases/).

## Installation instructions

Install Django:

```sh
pip install django
```

Clone this repository:

```
https://github.com/endormi/django.git
```

> `cd` into boilerplate

Migrate:

```sh
py manage.py migrate
```

Run the server:

```sh
py manage.py runserver
```

**To rename folders, you need to rename boilerplate and starter in `.py` files:**

`manage.py`

```python
os.environ.setdefault('boilerplate.settings')
```

`settings.py`

```python
INSTALLED_APPS = [
    'starter',
]
```

`urls.py`

```python
from starter import views

urlpatterns = [
    path('', include('starter.urls')),
]
```

`wsgi.py`

```python
os.environ.setdefault('boilerplate.settings')
```

`apps.py`

```python
class StarterConfig(AppConfig):
    name = 'starter'
```

### More documentation coming soon..

Looking for contributors to help with adding more content and better documentation.
