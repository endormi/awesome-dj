# django

> 📋 List of reasons why django is awesome for web development

Before making a commit read [contribution guidelines](https://github.com/endormi/django/blob/master/CONTRIBUTING.md)

Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

To give you an idea what the capabilities of Django are, here is a list of big companies that use Django.

1. [Disqus](https://disqus.com/)
2. [Instagram](https://www.instagram.com/)
3. [Spotify](https://www.spotify.com/)
4. [YouTube](https://www.youtube.com/)
5. [The Washington Post](https://www.washingtonpost.com/)
6. [Dropbox](https://www.dropbox.com/)
7. [BitBucket](https://bitbucket.org/)
8. [Mozilla](https://www.mozilla.org/)

## Building web applications ⛏

## Security 🔒

By default, Django prevents most common security mistakes:

* [XSS](https://docs.djangoproject.com/en/2.1/topics/security/#cross-site-scripting-xss-protection) (cross-site scripting) protection — Django template system by default escapes variables, unless they are explicitly marked as safe.

* [CSRF](https://docs.djangoproject.com/en/2.1/topics/security/#cross-site-request-forgery-csrf-protection) (cross site request forgery) protection — easy to turn on globally, guarantees that forms (POST requests) are sent from your own site.

* [SQL](https://docs.djangoproject.com/en/2.1/topics/security/#sql-injection-protection) injection protection — Django uses built-in ORM, thus there is no risk of SQL injection (raw queries are possible, but by no means something that a beginner would need to use).

* [PBKDF2](https://docs.djangoproject.com/en/2.1/topics/auth/passwords/#how-django-stores-passwords) password hashing - Django uses the PBKDF2 algorithm with a SHA256 hash, a password stretching mechanism recommended by NIST. It’s quite secure, requiring massive amounts of computing time to break.

## Packages 📦

Like the Python community in general, the Django community contributes useful packages and utilities for use by the wider world. Searching for “django” on PyPI finds over 3,000 packages available for use. This is on top of Django’s “batteries included” mentality. The framework has already included most things you’re going to want.

A list of awesome packages (not in a specific order):

1. [django-allauth](https://pypi.org/project/django-allauth/)
2. [django-contact-form](https://pypi.org/project/django-contact-form/)
3. [django-filter](https://pypi.org/project/django-filter/)
4. [django-rest-framework](https://www.django-rest-framework.org/)
5. [django-tables2](https://pypi.org/project/django-tables2/)
6. [pillow](https://pillow.readthedocs.io/en/latest/)
7. [httpie](https://httpie.org/)

## Documentation 📑

When it first came out, one of the features that set Django apart was how good the documentation was. Many other frameworks just used an alphabetical list of modules and all the attributes and methods. This is great for quick reference when you just can’t remember if it’s `array_sort()` or `sort_array()`. It doesn’t help, though, when you’re first learning the framework.

Django’s documentation quality may not be unique any more. It’s definitely still one of the best examples of open source documentation in the wild. And keeping these docs to this quality level is still a concern for Django’s developers. Docs are a first-class citizen in the Django world.

## Solving issues 🔎
