# How to run docker commands without sudo

To avoid using sudo for Docker commands, you can add your user to the docker group. This allows you to run Docker commands without sudo.

## Step 1. Add Your User to the Docker Group

SSH into your Ubuntu VM and run the following command:

```bash
sudo usermod -aG docker $USER
```

This adds your current user ($USER) to the docker group.

## Step 2. Log out and log back in

After running the command, you need to log out and log back into the VM for the changes to take effect:

```bash
exit
```

Then SSH back into the VM:

```bash
ssh your-username@192.168.1.146
```

## Step 3. Verify that your user is in the Docker group

Run the following command to check if your user has been added to the docker group:

```bash
groups
```

You should see docker listed as one of the groups.

## Step 4. Run Docker commands without sudo

Now you should be able to run Docker commands without needing sudo:

```bash
docker compose build
docker compose up -d
```
