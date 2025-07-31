#!/usr/bin/env bash

# Exit on error
set -o errexit

pip install -r requirements.txt

# Collect static files for Render to serve
python manage.py collectstatic --noinput
