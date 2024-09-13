# django-starter-template


## Overview

This is a Django Dockerized Production-Ready starter template. Goals is to make life eas for develoeprs so that they can focus on development and business logic, by minimizing the hassle of setup and deployment.

This starter template consists of the following services:

* Django app
* PostgreSQL (actually Postgis) database
* Redis Cache
* Celery and Redis

## Split settings for different environments

We create a settings folder and a split between settings files

* base.py -> renamed settings.py file and moved part ofthe contents to either development.py, prpduction.py or both
* development.py
* production.py

## Environment Variables

An .env file that allows you to describe different environments (production and development)

## Entrypoint to ensure Postgress is healthy befor Django is starterd

There is a script (entrypoint.sh) to ensure Postgres is healthy befor Django is started.
This script uses netcast.