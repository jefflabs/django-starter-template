# How to run Docker test environment on proxmox

Got it! You want to deploy a Docker container from your Mac to your Ubuntu VM on Proxmox. Here's a step-by-step guide on how to achieve that:

## 1: Ensure Docker is Installed on Your Ubuntu VM

First, make sure Docker is installed and running on your Ubuntu VM assumiong the following ip: 192.168.1.146

### Step 1: SSH into Your Ubuntu VM

From your Mac, SSH into the Ubuntu VM:

ssh your-username@192.168.1.146

### Step 2: Install Docker on Ubuntu (if not already installed)

Once you're logged in, run the following commands to install Docker if it isn't installed:

```bash
# Update existing packages
sudo apt update

# Install required packages
sudo apt install apt-transport-https ca-certificates curl software-properties-common

# Add Docker’s official GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# Set up the stable Docker repository
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

# Update the package database again with Docker’s packages
sudo apt update

# Install Docker
sudo apt install docker-ce

# Start Docker service and enable it on boot
sudo systemctl enable docker
sudo systemctl start docker
```

### Step 3: Install Docker Compose (if using it)

If you're also using Docker Compose, you can install it by running the following commands:

```bash
# Download the latest version of Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/v2.16.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# Apply executable permissions
sudo chmod +x /usr/local/bin/docker-compose

# Check the installation
docker-compose --version
```

## 2. Set Up SSH Access Between Your Mac and the Ubuntu VM

To automate deployment from your Mac to the Ubuntu VM, you should set up passwordless SSH access.

### Step 1: Generate SSH Keys (if you don’t have them)
On your Mac, generate SSH keys if you haven't already:

```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

This will generate a public/private key pair in ~/.ssh/id_rsa and ~/.ssh/id_rsa.pub.

### Step 2: Copy SSH Key to the Ubuntu VM

Next, copy your public key to the Ubuntu VM for passwordless login:

```bash
ssh-copy-id your-username@192.168.1.146
ssh-copy-id jeffrey@192.168.1.107
```

You should now be able to SSH into your VM without entering a password.

## 3. Transfer Docker Compose Files to the Ubuntu VM
You can now transfer your docker-compose.yml and any other necessary files to the Ubuntu VM. One simple way to do this is by using scp (Secure Copy Protocol):

### Step 1: Copy Files from Mac to Ubuntu VM

From your Mac, run the following command to transfer your Docker Compose files:

scp -r /path/to/your/files your-username@192.168.1.146:/path/on/ubuntu/vm/

For example if your username is jeffrey:

```bash
scp -r ./. user@192.168.1.146:/home/jeffrey/app/
```

This will copy the docker-compose.yml file to the app directory on your Ubuntu VM.

## 4. Build and Run Docker Containers on the Ubuntu VM

Now that your Docker Compose file is on the VM, you can SSH into the Ubuntu VM and run your Docker containers.

### Step 1: SSH Into the Ubuntu VM

On your Mac, SSH into the Ubuntu VM:

```bash
ssh your-username@192.168.1.146
```

### Step 2: Navigate to the Directory with Docker Compose Files

Navigate to the directory where you transferred your file:

```bash
cd /path/on/ubuntu/vm/app
```

### Step 3: Build and Run Docker Containers

Now, you can run the following Docker Compose commands to build and run the containers:

```bash
# Build the Docker containers
docker-compose build

# Run the Docker containers
docker-compose up -d
```

The -d flag runs the containers in detached mode (in the background). If you want to see the logs, run:

```bash
docker-compose logs -f
```

### Optional: How to run docker commands without sudo

-> see "How to run docker commands without sudo.md"

## 5. Optional: Automate the Process

If you want to automate this process further, you can create a simple shell script on your Mac to handle the transfer and deployment steps.

Example Shell Script (deploy.sh)
Create a deploy.sh script on your Mac that automates copying the files and running Docker Compose:

```bash
#!/bin/bash

# Define variables
USER="your-username"
HOST="192.168.1.146"
TARGET_DIR="/path/on/ubuntu/vm/app"

# Step 1: Copy Docker Compose files to the Ubuntu VM
scp -r ./docker-compose.yml $USER@$HOST:$TARGET_DIR

# Step 2: SSH into the Ubuntu VM and build/run the containers
ssh $USER@$HOST << EOF
  cd $TARGET_DIR
  docker-compose build
  docker-compose up -d
EOF

echo "Deployment complete."
```

Make it executable:

```bash
chmod +x deploy.sh
```

You can now run this script to transfer your files and deploy the containers automatically:

```bash
./deploy.sh
```

## 6. Test and Access Your Application

Once the containers are running on your Ubuntu VM, you can access your application using the IP address of the Ubuntu VM (192.168.1.146). If your Docker Compose file exposes a port (e.g., 80 for HTTP), you can open the application in a browser:

```bash
http://192.168.1.146:80
```

Make sure that the ip address of your ubuntu vm (in this example: 192.168.1.146) is part of the allowed hosts.
Make sure your Ubuntu VM’s firewall (if enabled) allows access to the necessary ports.


## Summary:
* Install Docker and Docker Compose on your Ubuntu VM.
* Set up SSH keys for passwordless access between your Mac and the Ubuntu VM.
* Transfer your Docker Compose files to the Ubuntu VM using scp.
* Build and run the Docker containers on the Ubuntu VM using docker-compose.
* Optionally, automate the process with a deployment script.