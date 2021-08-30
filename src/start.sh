#!/bin/bash
if [ -d "/var/hrobbin/django_blog" ]
then
    echo "django already installed" && /bin/bash
else
    mkdir django_blog && cd django_blog && python3.9 -m venv ./env && source ./env/bin/activate && pip install django && /bin/bash
fi