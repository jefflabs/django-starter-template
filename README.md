# django-starter-template


## Overview

This is a Django Dockerized Production-Ready starter template. Goals is to make life eas for develoeprs so that they can focus on development and business logic, by minimizing the hassle of setup and deployment.

This starter template consists of the following services:

* Django app
* PostgreSQL (actually Postgis) database
* Redis Cache
* Celery and Redis Messagebroker
* Gunicorn
* Nginx

## Split settings for different environments

We create a settings folder and a split between settings files

* base.py -> renamed settings.py file and moved part ofthe contents to either development.py, prpduction.py or both
* development.py
* production.py

## Environment Variables

An .env file that allows you to describe different environments (production and development)

## PostgreSQL Database

We add a PostgreSQL (actually a PostGIS for geospatial stuff) database and an entrypoint to ensure Postgress is healthy befor Django is starterd.

The script (entrypoint.sh) is there to ensure Postgres is healthy befor Django is started. This script uses netcast.

## Celery and Redis

We add celery for time-intensive asynchronuous tasks that can run in the background. So that the frontend is not waiting for these user requests. Redis is used as the message broker. We use redis since it can also be used as cache.

## Hardeing Docker compose for production -> Gunicorn and Nginx

We replaced Django's built-in webserver with Gunicorn. We added Nginx to act as a reverse proxy for Gunicorn and serve static files.

Furthermore in web we replaced prorts by expose this allows the web service to be exposed to other servicres inside Docker but not to the host machine.

We created a docker-compose.prod.yml file for production.
NB docker-compose.yml is used for development.
