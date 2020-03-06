#!/bin/bash

pip install django
python manage.py migrate
python manage.py runserver
