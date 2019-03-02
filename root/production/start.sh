#!/usr/bin/env bash
python3 /app/backend/root/manage.py makemigrations
python3 /app/backend/root/manage.py migrate

python3 /app/backend/root/manage.py initadmin

/usr/local/bin/gunicorn teddycrepineau.wsgi -b 0.0.0.0:8000 --chdir=/app/backend/root/