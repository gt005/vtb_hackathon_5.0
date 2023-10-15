#!/bin/bash

set -e

python manage.py migrate
python manage.py collectstatic --noinput
python generate_db/clear_database_instances.py
python generate_db/parser_handler.py
python generate_db/generate_data.py
python manage.py runserver 0.0.0.0:8000
