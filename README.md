# django

> 📋 List of reasons why django is awesome for web development

Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

To give you an idea what the capabilities of Django are, here is a list of big companies that you use Django.

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

## Documentation 📑

## Solving issues 🔎