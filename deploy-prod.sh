#!/bin/bash

# Define variables
USER="jeffrey"
HOST="192.168.1.107"
TARGET_DIR="/home/jeffrey/app"

# Step 1: Copy files to the Ubuntu VM
# scp -r ./. $USER@$HOST:$TARGET_DIR
scp -r app_home/ app_users/ config/ nginx/ static/ templates/ .dockerignore .env.prod docker-compose.prod.yml Dockerfile entrypoint.sh manage.py requirements.txt $USER@$HOST:$TARGET_DIR
# rsync -av --files-from=<(git ls-files) ./ $USER@$HOST:$TARGET_DIR

# Step 2: SSH into the Ubuntu VM and rename files, then build/run the containers
ssh $USER@$HOST << EOF
  cd $TARGET_DIR
  
  # Rename docker-compose.prod.yml to docker-compose.yml
  cp docker-compose.prod.yml docker-compose.yml
  
  # Rename .env.prod to .env
  cp .env.prod .env

  # Export DJANGO_ENV and build/run containers
  export DJANGO_ENV=production
  docker compose build
  docker compose up -d
EOF

echo "Deployment complete."
