# Using MySQL with Django

Install `mysqlclient`:

```sh
pip install mysqlclient
```

Add this to your `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/path/to/my.cnf',
        },
    }
}
```

My.cnf:

```
[client]
database = NAME
user = USER
password = PASSWORD
default-character-set = utf8
```

Remove migrations (this is needed, because the current migrations are linked to `sqlite3`).

Migrate:

```sh
python manage.py migrate
```
