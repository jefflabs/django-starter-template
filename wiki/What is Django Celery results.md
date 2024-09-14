# Django Celery results

## Overview

The package django-celery-results provides a way to store and manage the results of Celery tasks in a Django application. It enables you to store the task states and return values (results) in your database, making it easy to track the status and output of Celery tasks.

## Key Features of django-celery-results

* Result Storage: It allows Celery task results to be stored in a Django-supported database (like PostgreSQL, MySQL, or SQLite) by leveraging Django’s ORM.
* Task State Tracking: You can track the state of tasks, including success, failure, and pending states, along with storing exceptions if a task fails.
* Task Result Expiration: Task results can expire after a configurable time period, preventing the database from accumulating too much data over time.
* Admin Interface: The task results are visible in the Django admin interface, which makes it easier to manage and review task outcomes.

## Common Use Cases

* Background Processing: When you need to run long-running tasks in the background (e.g., sending emails, data processing).
* Task Monitoring: If you want to monitor the status of asynchronous tasks, such as checking if a task is completed or if it failed.
* Result Access: To retrieve and use the results of completed tasks later in your application.

## How django-celery-results Works

When a Celery task finishes, its result is stored in the Django database. This result is accessible via the task ID, and you can query the results in your Django app. You can also view the task results in the Django admin panel if you register the appropriate model (TaskResult).
