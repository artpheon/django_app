#!/bin/bash
cd django_blog && \
pip install django && \
django-admin startproject django_blog . && django-admin startapp blog && \
python manage.py migrate
