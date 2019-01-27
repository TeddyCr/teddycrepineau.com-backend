#!/usr/bin/env bash
python3 /app/root/manage.py migrate
python3 /app/root/manage.py collectstatic --noinput
python3 /app/root/manage.py runserver 0.0.0.0:8000