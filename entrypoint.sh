#!/bin/sh

echo 'Waiting for postgres...'

echo "Checking connection to database at $DB_HOSTNAME:$DB_PORT..."

while ! nc -zv $DB_HOSTNAME $DB_PORT; do
    echo "Still waiting for database to be available at $DB_HOSTNAME:$DB_PORT..."
    sleep 0.1
done

echo "Database is available at $DB_HOSTNAME:$DB_PORT!"

echo 'Running makemigrations...'
python manage.py makemigrations

echo 'Running migrations...'
python manage.py migrate

# Create static and media directories if they don't exist
echo 'Ensuring static and media directories exist...'
mkdir -p /code/staticfiles
mkdir -p /code/mediafiles

# Collect static files
echo 'Collecting static files...'
python manage.py collectstatic --no-input

echo 'Creating superuser if not exists...'
python manage.py shell <<EOF
import os
from django.contrib.auth import get_user_model
from app_users.models import Profile  # Import your Profile model

User = get_user_model()

superuser_username = os.getenv('DJANGO_SUPERUSER', 'admin')
superuser_email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'admin@admin.com')
superuser_password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'mikdik')

# Create superuser if not exists
if not User.objects.filter(username=superuser_username).exists():
    superuser = User.objects.create_superuser(username=superuser_username, password=superuser_password, email=superuser_email)
    print(f"Superuser '{superuser_username}' created successfully.")

    # Manually create the profile for the superuser
    Profile.objects.create(user=superuser)
    print(f"Profile for superuser '{superuser_username}' created successfully.")
else:
    print(f"Superuser '{superuser_username}' already exists.")
EOF

exec "$@"
