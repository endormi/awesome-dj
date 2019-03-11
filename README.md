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

The Django project's stability, performance and community have grown tremendously over the past decade since the framework's creation. Detailed tutorials and good practices are readily available on the web and in books. The framework continues to add significant new functionality such as `database migrations` with each release.

## Building web applications ⛏

Django's primary goal is to ease the creation of complex, database-driven websites. The framework emphasizes reusability and `"pluggability"` of components, less code, low coupling, rapid development, and the principle of don't repeat yourself. Python is used throughout, even for settings files and data models. Django also provides an optional administrative create, read, update and delete interface that is generated dynamically through introspection and configured via admin models.

Django has adopted Python’s `“batteries included”` approach — the framework has everything necessary to develop a fully fledged application out of the box.

You don’t need to spend hours customizing it to build a simple application or a prototype since all of the essentials are already available. But if you need additional features for a more complex app, there are well over 4,000 packages for Django to cover profiling, testing, and debugging. The framework also has tool packages for working with cutting-edge technology such as data analysis, AI, and machine learning.

Django's structure mainly consists of:

1. The Model Layer
2. The Views Layer
3. The Template Layer 
4. The Development Process
5. Security
6. The Admin
7. Forms

### Scalable

Another area in which Django stands out as being ideal for many developers is scalability. When you need an app that can grow in depth and complexity to any scale and is capable of handling as many visitors and/or transactions as demanded, Django shines. At its core, Django is just a series of components of Python, wired up and ready to go. Since these components are separate entities, they’re not dependent on each other. You can pick and choose, unplug and replace them as and when your site requires. This means you can build it up to whatever level of performance you need your site to be capable of, at any time, without compromising the functionality of the website.

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
3. [django-compressor](https://django-compressor.readthedocs.io/en/stable/)
4. [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/)
5. [django-filter](https://pypi.org/project/django-filter/)
6. [django-rest-framework](https://www.django-rest-framework.org/)
7. [django-tables2](https://pypi.org/project/django-tables2/)
8. [django-taggit](https://django-taggit.readthedocs.io/en/latest/)
9. [pillow](https://pillow.readthedocs.io/en/latest/)
10. [httpie](https://httpie.org/)
11. [django-sorting-field](https://pypi.org/project/django-sorting-field/)
12. [django-environ](https://django-environ.readthedocs.io/en/latest/)
13. [django-fsm](https://github.com/viewflow/django-fsm)

## Documentation 📑

Django’s official documentation is more than enough for developers. You can easily find solutions if you get stuck. On top of that, Stack Overflow is flooded with questions & answers related to Django.

## Open Source Community 🗃

Being open source and insanely popular, Django has created a helpful community. I’m assuming you’re aware of the advantages of open source software. Django has the same advantages.

So far we’ve seen that Django created a lot of libraries of its own, so it might surprise you that it didn’t create any library for testing. It doesn’t mean that Django framework doesn’t support testing — it does. They have a complete section dedicated to testing in docs. Following the principle “Don’t reinvent the wheel”, it’d be pointless to develop a testing library when Python itself provides a great one itself. Django just plays nice with it. It also works well with other popular third-party libraries like pytest.

Django is the perfect balance between performance, architecture, development effort, security and scalability.
