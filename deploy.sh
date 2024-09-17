#!/bin/bash

# Define variables
USER="jeffrey"
HOST="192.168.1.146"
TARGET_DIR="/home/jeffrey/app"

# Step 1: Copy files to the Ubuntu VM
# scp -r ./. $USER@$HOST:$TARGET_DIR
rsync -av --files-from=<(git ls-files) ./ $USER@$HOST:$TARGET_DIR


# Step 2: SSH into the Ubuntu VM and build/run the containers
ssh $USER@$HOST << EOF
  cd $TARGET_DIR

  # Rename docker-compose.prod.yml to docker-compose.yml
  cp docker-compose.test.yml docker-compose.yml
  
  # Rename .env.test to .env
  cp .env.prod .env

  docker-compose -f docker-compose.yml build
  docker-compose up -d
EOF

echo "Deployment complete."
