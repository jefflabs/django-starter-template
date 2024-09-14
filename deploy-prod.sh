#!/bin/bash

# Define variables
USER="jeffrey"
HOST="192.168.1.146"
TARGET_DIR="/home/jeffrey/app"

# Step 1: Copy Docker Compose files to the Ubuntu VM
scp -r ./. $USER@$HOST:$TARGET_DIR

# Step 2: SSH into the Ubuntu VM and build/run the containers
ssh $USER@$HOST << EOF
  cd $TARGET_DIR
  docker-compose -f docker-compose.prod.yml build
  docker-compose up -d
EOF

echo "Deployment complete."
