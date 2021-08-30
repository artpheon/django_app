#!/bin/bash
if [ -d "/var/hrobbin/django_blog" ]
then
    echo "env already created" && /bin/bash
else
    mkdir django_blog && python3.9 -m venv ./django_blog/env && /bin/bash
fi