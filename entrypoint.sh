#!/bin/sh

# Script to ensure Postgres is healthy befor Django is started

echo 'Waiting for postgres...'

while ! nc -z $DB_HOSTNAME $DB_PORT; do
    sleep 0.1
done

echo 'PostgreSQL started'

echo 'Running migrations...'
python managae.py migrate

echo 'Collect static files...'
python managae.py collectstatic --no-input

exec "$@"