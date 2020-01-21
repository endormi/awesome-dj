# Using PostgreSQL with Django

Install `psycopg2`:

```sh
pip install psycopg2
```

Add this to your `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'name',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'LOCALHOST',
        'PORT': '5432'
    }
}
```

Remove migrations (this is needed, because the current migrations are linked to `sqlite3`).

Migrate:

```sh
python manage.py migrate
```
