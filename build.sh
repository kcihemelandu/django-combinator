#!/usr/bin/env bash
# exit on error

set -o errexit

pip install --upgrade pip;
pip install Django gunicorn uvicorn whitenoise;
python manage.py collectstatic --no-input
python manage.py migrate
