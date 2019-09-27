# Django-Bootstrap-Boilerplate

Boilerplate for Django (**2.1.7**) using Bootstrap **4.3.1**

> Easy-to-use Boilerplate. Including three **HTML** templates `base.html`, `index.html` and `about.html`. The db used is `sqlite3`.

## Installation instructions

Clone this repository:

```
https://github.com/endormi/django.git
```

> `cd` into boilerplate

Install requirements:

```sh
pip install -r requirements.txt
```

Migrate:

```sh
py manage.py migrate
```

Run the server:

```sh
py manage.py runserver
```

**To rename folders you need to rename boilerplate and starter in `.py` files:**

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
