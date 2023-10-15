#!/bin/bash

set -e

python manage.py migrate
python manage.py collectstatic --noinput
python parser_handler.py
python generate_data.py
python manage.py runserver 0.0.0.0:8000
