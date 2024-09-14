# django-starter-template

## Overview

This is a Django Dockerized Production-Ready starter template. Goals is to make life eas for develoeprs so that they can focus on development and business logic, by minimizing the hassle of setup and deployment.

This starter template consists of the following services:

* Django app
* PostgreSQL database
* Redis Cache
* Celery and Redis Messagebroker
* Gunicorn
* Nginx

Status: tested and works

### TODOs

* TODO: split .env file in a production and development file
* TODO: create a seperate compose and entrypoint directory -> cleaner then everythin in the root
* TODO: create seperate base, production and development requirement.txt files
* TODO: create home app -> and a home page includig header menu
* TODO: add django allauth + pillow (for avatar image)

### Getting the files

Clone with git and remove git folder

```bash
git clone https://github.com/jseverijn3k/django-starter.git . && rm -rf .git
```

## Split settings for different environments

We create a settings folder and a split between settings files

* base.py -> renamed settings.py file and moved part ofthe contents to either development.py, prpduction.py or both
* development.py
* production.py

## Environment Variables

An .env file that allows you to describe different environments (production and development)

## PostgreSQL Database

We add a PostgreSQL database and an entrypoint to ensure Postgress is healthy befor Django is starterd.

The script (entrypoint.sh) is there to ensure Postgres is healthy befor Django is started. This script uses netcast.

## Celery and Redis

We add celery for time-intensive asynchronuous tasks that can run in the background. So that the frontend is not waiting for these user requests. Redis is used as the message broker. We use redis since it can also be used as cache.

## Gunicorn and Nginx

We are hardeing Docker compose for production by replacing Django's built-in webserver with Gunicorn (also done for development). We added Nginx to act as a reverse proxy for Gunicorn and serve static files.

Furthermore in web we replaced prorts by expose this allows the web service to be exposed to other servicres inside Docker but not to the host machine.

We created a docker-compose.prod.yml file for production.

NB docker-compose.yml is used for development.

## Deploying to a testserver

See the wiki (How to run docker test environment on proxmox)
on how to deploy docker on a proxomox-ubuntu test environment.

The deploy.sh script can be used to automate the deployment.

Make it executable:

```bash
chmod +x deploy.sh
```

You can now run this script to transfer your files and deploy the containers automatically:

```bash
./deploy.sh
```

Note: don't forget to change the variables in this cript.