#!/bin/sh

echo 'Waiting for postgres...'

echo "Checking connection to database at $DB_HOSTNAME:$DB_PORT..."

while ! nc -zv $DB_HOSTNAME $DB_PORT; do
    echo "Still waiting for database to be available at $DB_HOSTNAME:$DB_PORT..."
    sleep 0.1
done

echo "Database is available at $DB_HOSTNAME:$DB_PORT!"

echo 'Running migrations...'
python manage.py migrate

echo 'Collecting static files...'
python manage.py collectstatic --no-input

exec "$@"